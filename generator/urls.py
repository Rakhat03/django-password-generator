from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('password/', password, name='password'),
    path('about/', about, name='about'),
]