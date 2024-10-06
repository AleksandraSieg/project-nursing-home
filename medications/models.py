# Create your models here.
from django.db import models

class Medication(models.Model):
    trade_name = models.CharField(max_length=100)  # Nazwa handlowa
    international_latin_name = models.CharField(max_length=100)  # Nazwa międzynarodowa (łacińska)

    def __str__(self):
        return self.trade_name
