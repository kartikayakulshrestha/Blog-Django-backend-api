from rest_framework import serializers
from api.models import User,Blog,likes,comments,userV2

from django.db.models import Count
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= comments
        fields="__all__"
    
class BlogSerializer(serializers.ModelSerializer):
    num_comments = serializers.SerializerMethodField()
    num_likes = serializers.SerializerMethodField()
    comment=serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'author', 'create_at', 'num_comments', 'num_likes','comment']

    def get_num_comments(self, obj):
        return obj.comments_set.count()

    def get_num_likes(self, obj):
        return obj.likes_set.count()
    def get_comment(self, obj):
        latest_comment =  obj.comments_set.all().order_by('-create_at')[:5]
        if latest_comment:
            serializer = commentsSerializer(instance=latest_comment ,many=True)
            return serializer.data
        return []
    

        
class likerSerializer(serializers.ModelSerializer):
    class Meta:
        model= likes
        fields="__all__"

#version 2
class userv2Serializer(serializers.ModelSerializer):
    class Meta:
        model= userV2
        fields="__all__"
        extra_kwags={'blogger':{'required':True}}

