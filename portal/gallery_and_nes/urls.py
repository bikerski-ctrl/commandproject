from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('photos/', views.photo_gallery, name='photo_gallery'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('add-photo/', views.add_photo, name='adding_photo'),
    path('delete/<int:pk>/', views.DeletePhotoView, name='delete_photo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)