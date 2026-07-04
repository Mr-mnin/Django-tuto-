from django.urls import path
from . import views

urlpatterns = [
    path("currency0/", views.currency0, name="currency0"),
    path("currency1/", views.currency1, name="currency1"),
    path("api/rates/", views.currency_proxy, name="currency_proxy"),
]
