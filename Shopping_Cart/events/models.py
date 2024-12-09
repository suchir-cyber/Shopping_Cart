from django.db import models
from accounts.models import Vendor
from django.contrib.auth.models import User


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Membership(models.Model):
    DURATION_CHOICES = [
        ('6 months', '6 Months'),
        ('1 year', '1 Year'),
        ('2 years', '2 Years'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, default='6 months')

    def __str__(self):
        return f"{self.user.username} - {self.duration}"