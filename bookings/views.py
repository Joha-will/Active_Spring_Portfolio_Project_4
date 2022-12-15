from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Booking
from django.contrib import messages
from bookings.forms import CustomerForm


def index_page(request):
    return render(request, 'bookings/index.html')


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
            return redirect('booking')
    context = {'form': form}
    return render(request, 'bookings/create-booking.html', context)


def update_booking(request, booking_id):
    customer = get_object_or_404(Booking, booking_id=booking_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('booking')
    form = CustomerForm(instance=customer)
    context = {'form': form}
    return render(request, 'bookings/update-booking.html', context)