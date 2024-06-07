from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photo_gallery.html', {'photos': photos})

def video_gallery(request):
    videos = Video.objects.all()
    return render(request, 'video_gallery.html', {'videos': videos})


def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_gallery')  # Ensure this URL name matches your URLs configuration
    else:
        form = PhotoForm()
    
    return render(request, 'add_photo.html', {'form': form})

def DeletePhotoView(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('photo_gallery')

def DeleteVideoView(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_gallery')

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_gallery')
    else:
        form = VideoForm()
    
    return render(request, 'add_video.html', {'form': form})