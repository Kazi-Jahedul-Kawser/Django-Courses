from django.db import models
from categories.models import Categories
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    choices = [
        ('True','True'),
        ('False', 'False')
    ]
    is_completed = models.CharField(max_length=5, choices=choices, default='False')
    date = models.DateField()
    categories = models.ManyToManyField(Categories)