from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contact'),
    path('links/', views.links, name='links'),
    path('projects/', views.project, name='projects'),
]