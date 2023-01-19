from django.contrib import admin

# Register your models here.
from .models import Pokemon
# admin.site.register(Pokemon) this line without costimasitions
@admin.register(Pokemon) # if we want to custimoise the admin page
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hp' ,'active']
    list_display_links= ['id', 'name']
    # this changes happen in the admin page 
    list_filter =['active'] # this func help us to now which one is active 

    fieldsets = [ #we use this to coustimaze each items 
        ("localizatons", 

        {   "fields":['name_ar','name_fr','name_jp' ],
        
        }
        )
    ]