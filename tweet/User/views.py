from django.shortcuts import render
from .serializers import UserSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
