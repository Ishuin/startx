from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .forms import PostForm
from .models import Post, PostLike
from .serializers import PostSerializer, PostLikeSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post:post_list')


class PostLikeViewSet(ModelViewSet):
    serializer_class = PostLikeSerializer

    http_method_names = ['get', 'put', 'post', 'delete']

    def get_queryset(self):
        queryset = PostLike.objects.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        pk = request.data.get('post')
        ui = request.user.id
        serializer_class = PostLikeSerializer(data=request.data)
        if serializer_class.is_valid():
            try:
                post_det = PostLike.objects.get(post_id=pk, user_id=ui)
            except PostLike.DoesNotExist:
                post_det = None
            if post_det is None:
                serializer_class.save(post_id=pk, user_id=ui)
                post_obj = Post.objects.get(id=pk)
                post_obj.like_count += 1
                post_obj.save()
                return Response("Like Saved Successfully", status=HTTP_200_OK)
            else:
                return Response("Like already stored", status=HTTP_200_OK)
        else:
            return Response("Cannot Like the Post", status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        ui = request.user.id
        saved_likes = get_object_or_404(PostLike.objects.all(), id=self.kwargs['pk'], user=ui)
        post_obj = Post.objects.get(id=saved_likes.post_id)
        post_obj.like_count -= 1
        post_obj.save()
        saved_likes.deleted_on = timezone.now()
        saved_likes.delete()
        return Response({"message": "Like on post {} has been deleted.".format(saved_likes.post_id)}, status=204)
