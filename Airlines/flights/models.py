from django.db import models


class Airports(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # 'id' is automatically created by Django, no need to define it.
    origin = models.ForeignKey(
        Airports, on_delete=models.CASCADE, related_name="arrivals"
    )
    destination = models.ForeignKey(
        Airports, on_delete=models.CASCADE, related_name="departures"
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration}min"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
