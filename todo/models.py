from django.db import models
from django.utils import timezone


# Create your models here.


class Item(models.Model):
    item = models.CharField(max_length=200)
    date = models.DateField('date to be completed by')
    priority = models.IntegerField(default=0)
   

    def __str__(self):
        return self.item
    
    def due(self):
        return timezone.now().date() >= self.date
    due.boolean = True