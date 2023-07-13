from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>', views.SingleUserView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
