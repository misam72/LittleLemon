from django.db import models


class menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title

    def get_item(self):
        return f"{self.title}: {self.price}"


class booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
