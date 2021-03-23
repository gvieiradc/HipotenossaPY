from rest_framework import serializers
from pit.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'slug',
            'author',
            'body',
            'created'
        ]