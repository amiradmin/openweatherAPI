from django.contrib import admin
from weather.models import Weather
# Register your models here.

class WeatherAdmin(admin.ModelAdmin):
    list_display = ['id','city','temperature','datetime','created_at','updated_at']
    list_filter = ['id','city','temperature','datetime','created_at','updated_at']

admin.site.register(Weather,WeatherAdmin)
