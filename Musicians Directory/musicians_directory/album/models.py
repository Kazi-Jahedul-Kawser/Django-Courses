from django.db import models
from musicians.models import Musicians
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    musician = models.ForeignKey(Musicians, on_delete=models.CASCADE)
    date = models.DateField()
    rating_choices = [
        ('Poor' , 1),
        ('Average', 2),
        ('Better', 3),
        ('Good', 4),
        ('Excellent',5) 
    ]
    rating = models.CharField(max_length=20, choices=rating_choices)
    def __str__(self):
        return self.musician