from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name='likes_post')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='likes_user')
    activity = models.CharField(max_length=10, default='Like')

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return self.activity
