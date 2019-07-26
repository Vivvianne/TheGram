from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='thegram-home'),
    path('about/', views.about, name='thegram-about'),
]