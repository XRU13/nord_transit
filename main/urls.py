from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('services', views.services),
    path('assets', views.assets),
    path('contact', views.contact),
]
