from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    slug = models.SlugField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
