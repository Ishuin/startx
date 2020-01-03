from django.shortcuts import render
# from rest_framework.permissions import BasePermission
from .serializers import UserSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import User
from rest_framework import permissions


class UserViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset
