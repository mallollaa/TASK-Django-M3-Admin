from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.
class Pokemon (models.Model):
    name =  models.CharField(max_length=30 ,default= "" ,blank=True)
    type = models.CharField()
    hp = models.PositiveIntegerField
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30 , default="" ,blank=True)
    name_ar = models.CharField(max_length=30 , default="" ,blank=True)
    name_jp = models.CharField(max_length=30 , default="",blank=True)
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now_add=True)
class PokemonType(models.TextChoices):
        WATER = 'WA',
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'
Pokemon_Type= models.TextField(  
    max_length=30,
    choices= PokemonType.choices,
    default= PokemonType.WATER,
)
    
def is_upperclass(self):
    return self.PokemonType in {
        self.PokemonType.GHOST,
        self.PokemonType.STEEL,
}
