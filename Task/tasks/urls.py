from django.urls import path
from . import views

urlpatterns = [
    path('tasks0/', views.tasks0, name='tasks0'),
    path('tasks1/', views.tasks1, name='tasks1'),
    path('tasks2/', views.tasks2, name='tasks2'),
]