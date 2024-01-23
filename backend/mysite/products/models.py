from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField("date created", default=timezone.now)

