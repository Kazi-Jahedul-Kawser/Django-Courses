from django.db import models
# Create your models here.
class Musicians(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.IntegerField()
    instrument = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name