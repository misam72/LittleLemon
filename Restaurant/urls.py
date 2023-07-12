from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('users/', views.UserView.as_view()),
    path('user/<int:pk>', views.SingleUserView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
]
