from django.contrib.auth.models import User,Group
from django.db.models import fields
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url','username','email']
# --> 현재 그룹이 없어서 입력해도 빈 값으로 출력될것