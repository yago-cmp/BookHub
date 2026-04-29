from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class Profile_Serial(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['usernameP', 'bio', 'pfp', 'streak', 'achievements', 'joined']

class User_Serial(serializers.ModelSerializer):

    profile = Profile_Serial()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
    
    def create(self, dados): #altera o create, insere dados iniciais no profile também, ja linkando os dois atraves do signals
        dadosProfile = dados.pop('profile') #retira a profile dos dados e poe em dadosProfile
        user = User.objects.create_user(**dados) #cria a profile com os dados restantes

        profile = user.profile
        profile.usernameP = dadosProfile.get('usernameP')
        profile.bio = dadosProfile.get('bio')
        profile.pfp = dadosProfile.get('pfp')
        profile.save()

        return user

    def update(self, objeto, dados):
        dadosProfile = dados.pop('profile', None) #none é fallback, caso a requisicao nao tenha dados de profile

        password = dados.pop('password', None)
        if password:
            objeto.set_password(password) #metodo set_password (senhas nao sao passadas em string normal)

        for attr, value in dados.items():
            setattr(objeto, attr, value)
        objeto.save()

        if dadosProfile is not None:
            profile = objeto.profile
            for attr, value in dadosProfile.items():
                setattr(profile, attr, value)
            profile.save()

        return objeto
