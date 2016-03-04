from django.db import models

# Create your models here.
class Event(models.Model):
    evb_id = models.CharField(max_length=100, unique=True)
    body = models.TextField() #Storing json string in this field

    def __str__(self):
        return self.evb_id
