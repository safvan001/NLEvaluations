# serializers.py

from rest_framework import serializers
from .models import AndroidApp, UserProfile, UserTask

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = ('id', 'name', 'points','image','link','category','subcategory')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'profile_image', 'points_earned')

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ('id', 'user', 'app', 'screenshot')
