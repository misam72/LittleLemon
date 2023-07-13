from django.shortcuts import render
from rest_framework import generics
from .models import menu, booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated]


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class SingleUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class BookingView(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]


class SingleBookingView(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]
