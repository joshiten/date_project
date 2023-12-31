from django.db import models

# Create your models here.

class DateResponse(models.Model):
    response = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])

