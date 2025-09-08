from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father = models.CharField(max_length=50, default='Jahangir')
    address = models.TextField()
    
    
    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
