from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Restaurant import views


router = DefaultRouter(trailing_slash=False)
router.register(r"booking", views.BookingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('Restaurant.urls')),
    path('', include(router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
]
