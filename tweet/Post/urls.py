from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostLikeViewSet
from . import views

router = DefaultRouter()

router.register(r'likes', PostLikeViewSet, basename='post_likes')
router.register(r'', PostViewSet, basename='posts')


app_name = 'post'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<pk>/remove/', views.post_remove, name='post_remove'),
]
