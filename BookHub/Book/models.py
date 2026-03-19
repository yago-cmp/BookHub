from django.db import models
import uuid

class Book(models.Model):
    author_id = models.OneToOneField('Author', related_name='book')

    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=40)
    pages = models.IntegerField(default=0)    
    editor = models.CharField(max_length=30, blank = True, null = True)
    genre = models.CharField(max_length=30, blank = True, null = True)
    synopsys = models.TextField(blank=True, null=True)
    edition = models.CharField(blank = True, null = True)
    cover = models.ImageField(default='fallback.png', blank=True, null=True)
    year = models.DateTimeField(blank = True, null = True)

    def __str__(self): 
        return self.title
    
class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default_uuid=uuid.uuid4, editable=False)

    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    pic = models.ImageField(default='fallback.png', blank=True, null=True)

    def __str__(self):
        return self.name
    

