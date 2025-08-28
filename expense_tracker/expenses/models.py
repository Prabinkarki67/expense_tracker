from django.db import models

# Create your models here.
class Reg(models.Model):
    email=models.EmailField(max_length=100, unique=True)
    username = models.TextField(max_length=15)
    