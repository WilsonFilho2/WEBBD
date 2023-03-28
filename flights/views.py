from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": models.Flight.objects.all(),
    })


def flight(request, flight_id):
    flight = models.Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = models.Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = models.Flight.objects.get(id=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = models.Passenger.objects.get(id=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))