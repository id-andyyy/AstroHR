from astro_check.views import *
from django.urls import path

urlpatterns = [
    path('', astro_check, name='astro_check'),
]
