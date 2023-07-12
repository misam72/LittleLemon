from django.db import models

class menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return self.title + " - " + str(self.price) + " - " + str(self.inventory)

class booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return self.name + " - " + str(self.no_of_guests) + " - " + str(self.booking_date)