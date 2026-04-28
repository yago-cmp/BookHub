from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class Profile_Serial(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['username', 'bio', 'pfp', 'streak', 'achievments', 'joined']

class User_Serial(serializers.ModelSerializer):

    profile = Profile_Serial(read_only=True) # !!!!!!!!! voltar aqui

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

