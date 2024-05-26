from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    ISBN = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title