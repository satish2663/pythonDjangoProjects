from django.db import models

# Create your models here.

class Car(models.Model):
    #primary key
    brand = models.CharField(max_length = 30)
    year = models.IntegerField()

    def __str__(self):
        return f"car is {self.brand} {self.year}"
