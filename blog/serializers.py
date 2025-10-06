from rest_framework import serializers
from blog.models import Post, Category, Profile, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = "__all__"

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = "__all__"