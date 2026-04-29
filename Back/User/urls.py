from django.urls import path
from .views import UserProfileUpdateView, ValidacaoUserView


urlpatterns = [
    path('me/', UserProfileUpdateView.as_view()),
    path('validacao-user', ValidacaoUserView.as_view())
]