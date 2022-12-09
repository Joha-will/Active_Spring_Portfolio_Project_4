from django.shortcuts import render, HttpResponse
from django.views.generic import (TemplateView)
from .models import Booking


class BookingHome(TemplateView):
    template_name = 'booking.html'