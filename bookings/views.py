from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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


@login_required
def create_booking(request, **kwags):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been successfully created!')
            return redirect(reverse('bookings:booking'))
    context = {'form': form}
    return render(request, 'bookings/create-booking.html', context)


def update_booking(request, booking_id):
    customer = get_object_or_404(Booking, booking_id=booking_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been successfully updated!')
            return redirect(reverse('bookings:booking'))
    form = CustomerForm(instance=customer)
    context = {'form': form}
    return render(request, 'bookings/update-booking.html', context)


def delete_booking(request, booking_id):
    customer = get_object_or_404(Booking, booking_id=booking_id)
    customer.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Your booking was successfully cancelled!')
    return redirect(reverse('bookings:booking'))
