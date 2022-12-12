from django.shortcuts import render, HttpResponse
from django.views.generic import (TemplateView, ListView, CreateView)
from .models import Booking


def booking_home(request):
    return render(request, 'booking.html')


class CreateBooking(CreateView):
    model = Booking
    template_name = 'create-booking.html'
    fields = ['full_name','email']