from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import User_Serial

class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = User_Serial
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user