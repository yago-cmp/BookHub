from django.urls import path
from .views import UserProfileUpdateView


urlpatterns = [
    path('me/', UserProfileUpdateView.as_view(), name='me')
]