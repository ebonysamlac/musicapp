from datetime import datetime
from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)


    def __str__(self):
        return self.first_name
        

class Songs(models.Model):
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    myartists_id = models.IntegerField()
    
    def __str__(self):
        return self.title

class Lyrc(models.Model):
    Songs = models.ForeignKey(Songs, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000) 
    mysongs_id = models.IntegerField()

    def __str__(self):
        return self.content