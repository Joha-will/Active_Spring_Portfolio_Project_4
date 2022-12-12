from django.shortcuts import render, HttpResponse
from django.views.generic import (TemplateView, ListView, CreateView)
from .models import Booking
from django.contrib import messages


def booking_home(request):
    return render(request, 'booking.html')


class CreateBooking(CreateView):
    model = Booking
    template_name = 'create-booking.html'
    fields = ['full_name', 'email', 'no_of_persons', 'booking_date_time', 'phone_number']