from django.shortcuts import render, redirect, HttpResponse
from .models import Booking
from django.contrib import messages
from bookings.forms import CustomerForm


def booking_home(request):
    customers = Booking.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'booking.html', context)


def create_booking(request):
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'create-booking.html', context)