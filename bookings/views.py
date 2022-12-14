from django.shortcuts import render, redirect, HttpResponse
from .models import Booking
from django.contrib import messages
from bookings.forms import CustomerForm


def booking_home(request):
    customer = Booking.objects.all()
    context = {
        'customers': customer,
    }
    return render(request, 'bookings/booking.html', context)


def create_booking(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'bookings/create-booking.html', context)


def update_booking(request, pk):
    customer = Booking.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'bookings/update-booking.html', context)