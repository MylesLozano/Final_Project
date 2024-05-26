from django.db import models
import os

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    ISBN = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            old_image = Book.objects.get(pk=self.pk).image
        except Book.DoesNotExist:
            old_image = None

        super(Book, self).save(*args, **kwargs)

        if old_image and old_image != self.image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)