import requests
from django.shortcuts import render
from django.http import JsonResponse

def currency0(request):
    return render(request, 'currency/currency0.html')

def currency1(request):
    return render(request, 'currency/currency1.html')

def currency_proxy(request):
    response = requests.get("https://api.frankfurter.app/latest?from=USD")
    return JsonResponse(response.json())