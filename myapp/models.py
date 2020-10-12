from django.db import models
from django.db import models



class World(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


    def __unicode__(self):
        return str(self.location)

    world_mapping = {
        'name': 'NAME',
        'address': 'ADDRESS',
        'city': 'CITY',
        'state': 'STATE',
        'location': 'LOCATION',

    }

