from django.contrib.auth.models import AbstractUser
from django.db import models
from Book.models import Book
from django.conf import settings
import uuid

class User(AbstractUser):
    pass
    
class Profile(models.Model):
    #related name faz o acesso de profile atraves de user mais facil. por padrao ja e profile
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')
    profile = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True, null=True)
    pfp = models.ImageField(default='fallback.png', blank=True, null=True)
    streak = models.IntegerField(default=0)
    achievements = models.CharField(max_length=100, blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.username

class Follow(models.Model):
    follow = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ["follower","following"]

    def __str__(self): 
        return self.follower.username + ' follows ' + self.following.username
    
class ReadList(models.Model):
    readlist = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='readlist')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.profile.username + ' listed ' + self.book.title
    
    class Meta:
        unique_together = ["book", "profile"]
    
class BookLog(models.Model):
    booklog = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='booklogs')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='booklogs')
    pages_read = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)

    def __str__(self): 
        return str(self.pages_read) + ' pages of ' + self.book.title
    
    class Meta:
        unique_together = ["book", "profile"]

class Update(models.Model):
    update = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booklog = models.ForeignKey(BookLog, on_delete=models.CASCADE, related_name='updates')
    pages_today = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    review = models.BooleanField(default = False)
    obs = models.TextField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)

    def __str__(self): 
        return str(self.pages_today) + ' pages today of ' + self.booklog.book.title   