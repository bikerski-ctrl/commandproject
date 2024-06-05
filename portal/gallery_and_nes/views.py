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
    photo.delete()
    return redirect('photo_gallery')