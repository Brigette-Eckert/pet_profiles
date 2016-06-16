from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Human(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField()
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=255)
    bio = models.TextField()

#look into pillow for Image Field
#fix defaults--djmake && djrun not working

class Pet(models.Model):
    human = models.ForeignKey(Human)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    picture = models.ImageField()
    hobbies = models.CharField(max_length=1000)


