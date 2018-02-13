from django.db import models
from django.contrib.auth.models import Permission, User
from django.db import IntegrityError
class Platform(models.Model):
    name= models.CharField(max_length=250)
    cover = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Game(models.Model):
    name= models.CharField(max_length=250)
    genere = models.CharField(max_length=10)
    cover = models.ImageField()
    platform = models.ForeignKey(  Platform, models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name
class MyLibrary(models.Model):
    user = models.ForeignKey( User, models.SET_NULL,blank=True,null=True,)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.game.name
