from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework import permissions
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .forms import UserRegistrationForm
# from rest_framework.permissions import BasePermission
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('post:post_list')
    else:
        form = UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/register.html', context)
