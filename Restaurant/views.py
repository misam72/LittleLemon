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
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingView(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

# from rest_framework import viewsets, status
# from rest_framework.response import Response

# class BookView(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def partial_update(self, request, pk=None):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

#         book.delete()
#         return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
