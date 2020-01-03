from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name='likes_post')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='likes_user')
    activity = models.CharField(max_length=10, default='Like')

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return self.activity
