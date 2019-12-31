from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostLike
from .serializers import PostSerializer, PostLikeSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostLikeViewSet(ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer