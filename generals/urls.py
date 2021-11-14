from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about')
]