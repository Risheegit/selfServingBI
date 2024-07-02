
# Create your models here.
from django.db import models

class DropdownChoice(models.Model):
    dropdown1 = models.CharField(max_length=100)
    dropdown2 = models.CharField(max_length=100)
    dropdown3 = models.CharField(max_length=100)
    dropdown4 = models.CharField(max_length=100)

