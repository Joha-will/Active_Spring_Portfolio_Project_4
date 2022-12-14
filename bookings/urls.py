from . import views
from django.urls import path

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_home, name='booking'),
    path('create-booking/', views.create_booking, name='create'),
]