from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, default='')
    lasr_name = models.CharField(max_length=100, default='')
    email=models.EmailField
    password=models.CharField

    def __str__(self):
        return self.first_name
