from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    path("counter/", views.count, name="count"),
    path("task/", views.task, name="task"),
]
