from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def hello(request):
    return render(request, "count/hello.html")


def count(request):
    return render(request, "count/counter.html")

