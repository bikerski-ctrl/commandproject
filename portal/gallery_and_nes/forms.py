from django import forms
from .models import *

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['user', 'title', 'image']  # Usually, 'uploaded_at' is auto_now_add and should not be included in the form.