from django.shortcuts import render
from .models import *

def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photo_gallery.html', {'photos': photos})

def video_gallery(request):
    videos = Video.objects.all()
    return render(request, 'video_gallery.html', {'videos': videos})