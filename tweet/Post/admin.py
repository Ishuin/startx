from django.contrib import admin
from .models import Post, PostLike
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')