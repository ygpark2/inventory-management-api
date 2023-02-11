from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group

from .models import User


class CustomUserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class GroupSerializer(ModelSerializer):
    class Meta(object):
        model = Group
        fields = ('id', 'name')
