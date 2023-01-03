from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Booking

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages

from .forms import CustomerForm


# Home page view

def index_page(request):

    return render(request, 'bookings/index.html')


# Create booking view

@login_required(login_url="account_login")
def create_booking(request):
    """ This view gives users the ability to create bookings"""

    form = CustomerForm()

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():

            customer = form.save(commit=False)

            customer.user = request.user

            customer.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been successfully created!')

            return redirect(reverse('bookings:booking'))

    context = {'form': form}

    return render(request, 'bookings/create-booking.html', context)


# Booking home view

def booking_home(request):
    """ This view give users the ability to view their bookings"""

    current_user = request.user.id

    customer = Booking.objects.all().filter(user=current_user)

    context = {'customers': customer}

    return render(request, 'bookings/booking.html', context)


# Update booking view

@login_required(login_url="account_login")
def update_booking(request, booking_id):
    """ This view gives users the ability to update their bookings"""

    customer = get_object_or_404(Booking, booking_id=booking_id)

    form = CustomerForm(instance=customer)

    if request.method == 'POST':

        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():

            form.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been successfully updated!')

            return redirect(reverse('bookings:booking'))

    context = {'form': form}

    return render(request, 'bookings/update-booking.html', context)

# Delete booking view


def delete_booking(request, booking_id):
    """ This view gives users the ability to delete their bookings"""

    customer = get_object_or_404(Booking, booking_id=booking_id)

    customer.delete()

    messages.add_message(
        request, messages.SUCCESS,
        'Your booking was successfully cancelled!')

    return redirect(reverse('bookings:booking'))
