from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = False
    if post.like_count.filter(id=request.user.id).exists():
        is_liked = True
    return render(
        request,
        'post/post_detail.html',
        {
            'post': post,
            'is_liked': is_liked,
            'total_likes': post.total_likes,
        }
    )


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


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.like_count.filter(id=request.user.id).exists():
        post.like_count.remove(request.user.id)
        is_liked = False
    else:
        post.like_count.add(request.user.id)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
