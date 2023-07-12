from django.contrib.auth.models import User
from rest_framework import serializers
from .models import menu, booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ["name", "no_of_guests", "booking_date"]
