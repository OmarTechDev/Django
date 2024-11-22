from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Property(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='owner'
    )
    def __str__(self):
        return self.title

class Reservation(models.Model):
    name= models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client'
    )
    property= models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='property'
    )
    days = models.BigIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=11)
    start_date = models.DateField()
    end_date = models.DateField()
    is_paid = models.BooleanField()
    def __str__(self):
        return self.name
    
class MethodPayment(models.Model):
    title= models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_card'
    )
    def __str__(self):
        return self.title