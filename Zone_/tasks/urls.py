from django.urls import path
from . import views

app_name = "tasks"  # <--- Make sure this is here!

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
]
