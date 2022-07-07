from rest_framework import serializers
from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('text', 'group')
