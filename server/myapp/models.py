from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    confirm_pass=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
    
class Movie(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='static/upload/')
    
    def __str__(self):
        return self.description
    
    




    