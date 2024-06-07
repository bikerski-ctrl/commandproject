from django import forms
from .models import *

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['user', 'title', 'image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['user', 'title', 'image']