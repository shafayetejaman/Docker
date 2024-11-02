from django.db import models
from django.contrib.auth.models import User
from show_cars.models import Car

# Create your models here.


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    parched = models.DateTimeField(auto_now_add=True)
