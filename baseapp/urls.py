from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected, name='protected'),

    path('profile/', views.profile, name='profile'),
    path('users/', views.user_list, name='user_list'),
    path('users/search/', views.user_search, name='user_search'),
]
