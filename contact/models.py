from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# from ckeditor.fields import RichTextField
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")

    def __str__(self):
        return self.title
