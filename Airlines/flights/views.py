from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Passenger, Flight

def index(request):
    # FIXED: 'flight' is not defined; use the model 'Flight'
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight_obj = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight_obj,
        "passengers": flight_obj.passengers.all(),
        # Ensure 'non_passengers' matches the variable in your template
        "non_passengers": Passenger.objects.exclude(flights=flight_obj).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight_obj = Flight.objects.get(pk=flight_id)
        # FIXED: Use square brackets for POST data: request.POST["passenger"]
        # FIXED: Use model 'Passenger' (capitalized)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) 
        # FIXED: Field is named 'flights' (plural) in your models.py
        passenger.flights.add(flight_obj)
        # FIXED: Use 'args' (plural) and ensure the URL name matches urls.py
        return HttpResponseRedirect(reverse("flights", args=(flight_id,)))