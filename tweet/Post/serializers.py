from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author', 'like_count', 'created_date']
        extra_kwargs = {
            'author':
                {'read_only': True},
            'like_count':
                {'read_only': True},
            'created_date':
                {'read_only': True},
        }
