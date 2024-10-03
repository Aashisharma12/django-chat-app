from .views import *
from django.urls import path, include
from google import views as view

urlpatterns = [
   ....
   path('map',view.map, name="map"),
   ...
]