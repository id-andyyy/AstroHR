from astro_check.views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('astro_check/', astro_check, name='astro_check'),
    path('generate/', generate, name='generate'),
]
