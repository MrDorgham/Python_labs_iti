from django.db import models

# Create your models here.

# class bkinfo(models.Model):
#     Name = models.CharField(max_length=100)
#     BookDiscription = models.CharField(max_length=100)
#     Price = models.IntegerField(default=100)
#     amount = models.IntegerField(default=0)

class bkinfo(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"
