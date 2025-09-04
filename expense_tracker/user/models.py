from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    expensed_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username} - {self.expensed_price} on {self.product}"