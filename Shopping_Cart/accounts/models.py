from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name