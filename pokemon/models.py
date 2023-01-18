from django.db import models
from datetime import datetime

# Create your models here.
class Pokemon (models.Model):
    name =  models.CharField(max_length=30)
    type = models.CharField()

  
    class PokemonType(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'

    Pokemon_Type= models.CharField(  
        max_length=100,
        choices= PokemonType.choices,
        
    )

    hp = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30 , default="" ,blank=True)
    name_ar = models.CharField(max_length=30 , default="" ,blank=True)
    name_jp = models.CharField(max_length=30 , default="",blank=True)
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now=True)

