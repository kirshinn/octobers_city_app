from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.video_view, name='video'),
    path('stream/', views.stream_view, name='stream'),
]
