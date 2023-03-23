from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Flight)
admin.site.register(models.Airport)
