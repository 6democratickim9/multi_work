# from django.contrib.auth.models import User,Group
from django.db.models import fields
from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
                    'id',
                    'title',
                    'slug',
                    'description',
                    'content',
                    'create_date',
                    'modify_date'
                    ]


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url','username','email']
# --> 현재 그룹이 없어서 입력해도 빈 값으로 출력될것