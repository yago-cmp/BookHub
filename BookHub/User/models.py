from django.db import models
from django.conf import settings
import uuid
# Create your models here.


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=16)

    def __str__(self): 
        return self.email
    

class Profile(models.Model):
    #related name faz o acesso de profile atraves de user mais facil. por padrao ja e profile
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')

    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True, null=True)
    pfp = models.ImageField(default='fallback.png', blank=True, null=True)
    streak = models.IntegerField(default=0)
    achievements = models.CharField(max_length=100, blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.username

class Follow(models.Model):
    follow_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ["follower","following"]

    def __str__(self): 
        return self.follower.username + ' followed ' + self.following.username
    
