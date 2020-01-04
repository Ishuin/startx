from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    like_count = models.ManyToManyField(User, related_name="post_likes", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'pk': self.id})

    def total_likes(self):
        return self.like_count.count()
