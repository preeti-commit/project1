from django.shortcuts import render
from django.shortcuts import render, redirect
from myapp import models
from .models import World
# from django.contrib.gis.geoip import GeoIP
from django.http import HttpResponse
# import urllib

def index(request):
        return render(request,'index.html',{'index': World.objects.all()})


# def Location(request):
#     return render(request, 'location.html')

def insert(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        # geolocator = GoogleV3()
        # location = geolocator.reverse("28.619579599999998, 77.2046848")
        # import pdb
        # pdb.set_trace()
        world =World(name=request.POST['name'],
                address=request.POST['address'],
                city=request.POST['city'],
                state=request.POST['state'],
                location=request.POST['latitude']+'-'+request.POST['longitude'],)
        world.save()
    return redirect('/')


