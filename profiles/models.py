from django.contrib.auth.models import User
from django.db import models

class Human(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to=None)
    birthday = models.DateField(auto_now=True, editable=True)
    location = models.CharField(max_length=255)
    bio = models.TextField()


class Pet(models.Model):
    human = models.ForeignKey(Human)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    picture = models.ImageField(upload_to=None)
    hobbies = models.CharField(max_length=1000)


