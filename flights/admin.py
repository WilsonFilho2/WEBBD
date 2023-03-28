from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Airport)
admin.site.register(models.Passenger)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

admin.site.register(models.Flight, FlightAdmin)
