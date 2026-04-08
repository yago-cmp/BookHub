from django.db import models
import uuid
class Author(models.Model):
    author = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    pic = models.ImageField(default='fallback.png', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    genre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Editor(models.Model):
    editor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=250, blank=True, null=True)
    founded = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    authors = models.ManyToManyField(Author, through='Book_Author', related_name='books')
    title = models.CharField(max_length=40)
    pages = models.IntegerField(default=0)    
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, through='Book_Genre', related_name='books')
    synopsys = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=10, blank = True, null = True)
    cover = models.ImageField(default='fallback.png', blank=True, null=True)
    year = models.DateField(blank = True, null = True)

    def __str__(self): 
        return self.title
    
class Book_Author(models.Model):
    book_author = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self): 
        return self.author.name + ' é autor de ' + self.book.title
    

class Book_Genre(models.Model):
    book_genre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self): 
        return self.genre.name + ' é gênero de ' + self.book.title