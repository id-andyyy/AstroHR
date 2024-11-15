from loginsys.views import *
from django.urls import path

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
