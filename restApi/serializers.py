from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['amount']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'likes']


class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username']

class UserPostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ['posts']

