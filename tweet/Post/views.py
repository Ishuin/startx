from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostLike


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()


class PostLikeViewSet(ModelViewSet):
    queryset = PostLike.objects.all()
