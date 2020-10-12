from django.contrib import admin
from myapp import models


class WorldAdmin(admin.ModelAdmin):
    class Meta:
        model = models.World
admin.site.register(models.World, WorldAdmin)

