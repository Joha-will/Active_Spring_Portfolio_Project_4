from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

class BookingListView(ListView):
    model = Booking
    template_name = 'booking.html'