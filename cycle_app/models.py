from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Institute_info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    public=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Versity_life_cycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute=models.ForeignKey(Institute_info,on_delete=models.CASCADE)
    year=models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    event = RichTextUploadingField()
    public=models.BooleanField(default=False)
    

    def __str__(self):
        return self.semester
