from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Hw2_home'),
]