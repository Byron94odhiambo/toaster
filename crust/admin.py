from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Store,Cuisine

@admin.register(Store)
class StoreAdmin(OSMGeoAdmin):
    list_display = ('name','order')


admin.site.register(Cuisine)