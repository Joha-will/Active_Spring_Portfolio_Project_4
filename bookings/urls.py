from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.BookingHome.as_view(), name='booking')
]