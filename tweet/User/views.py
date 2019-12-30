from django.shortcuts import render
from .serializers import UserSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
