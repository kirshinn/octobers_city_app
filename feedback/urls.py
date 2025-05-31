from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.feedback_view, name='feedback_email'),
]
