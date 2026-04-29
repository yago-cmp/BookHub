from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import User_Serial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = User_Serial
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

User = get_user_model()
class ValidacaoUserView(APIView):


    permission_classes = [] #o usuario nao precisa estar logado

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        erro = {}

        if (email and User.objects.filter(email = email).exists()):
            erro['email'] = "email em uso"

        if (username and User.objects.filter(username = username).exists()):
            erro['username'] = "username em uso"
        
        if erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)