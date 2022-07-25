from django.urls import path
from .views import Home,About

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('About/',About.as_view(), name='about'),
]