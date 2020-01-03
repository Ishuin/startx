from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'', UserViewSet, basename='user')

app_name = 'users'

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', UserViewSet.list, name='user_list'),
    path('<int:pk>/', UserViewSet.get_queryset, name='user_detail'),
    path('new/', UserViewSet.create, name='user_new'),
    path('<int:pk>/edit/', UserViewSet.update, name='user_edit'),
    path('<pk>/remove/', UserViewSet.destroy, name='user_remove'),
]
