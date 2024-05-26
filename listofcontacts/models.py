from django.db import models
import os

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Delete old image file when updating to a new one
        try:
            old_image = Contact.objects.get(pk=self.pk).profile_image
        except Contact.DoesNotExist:
            old_image = None

        super(Contact, self).save(*args, **kwargs)

        if old_image and old_image != self.profile_image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)
    
    def delete(self, *args, **kwargs):
        # Delete associated image file if it exists
        if self.profile_image:
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
        super().delete(*args, **kwargs)
