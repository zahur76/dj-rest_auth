from django.contrib.auth.models import User
from .models import Test
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'name']