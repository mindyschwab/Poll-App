from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    who = models.CharField(max_length=150)
    what = models.CharField(max_length=150)
    where = models.CharField(max_length=100)
    when = models.CharField(max_length=150)
    why = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.what
    
# class Poll(models.Model):


# class Group(models.Model):