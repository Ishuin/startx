from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostLikeViewSet

router = DefaultRouter()

router.register(r'likes', PostLikeViewSet)
router.register(r'', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
