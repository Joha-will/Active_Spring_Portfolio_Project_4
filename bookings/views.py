from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.core.paginator import Paginator

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

    # Set form variable to CustomerForm
    form = CustomerForm()

    # Check if request equal to POST
    if request.method == 'POST':

        # Pass in POST request
        form = CustomerForm(request.POST)

        # Check if the form is valid before submit
        if form.is_valid():

            # Postpone save
            customer = form.save(commit=False)

            # Set Foreign key to user
            customer.user = request.user

            # Save to current user
            customer.save()

            # Displays successful message to user
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been successfully created!')

            # Redirect back to booking.html
            return redirect(reverse('bookings:booking'))

    # Pass form into context dictionary
    context = {'form': form}

    # Return and render create-booking.html
    return render(request, 'bookings/create-booking.html', context)


# Booking home view

def booking_home(request):
    """ This view give users the ability to view their bookings"""

    # Get logged-in user ID
    current_user = request.user.id

    # Filter user objects from database in relation to foreign key
    customer = Booking.objects.all().filter(user=current_user)

    # Set Paginator to 3 on customer
    paginator = Paginator(customer, 3)

    # Get the page number request
    page_number = request.GET.get('page')

    # Get page numbers for paginator
    page_obj = paginator.get_page(page_number)

    # Place page_obj into context dictionary
    context = {'page_obj': page_obj}

    # Return and render booking.html
    return render(request, 'bookings/booking.html', context)


# Update booking view

@login_required(login_url="account_login")
def update_booking(request, booking_id):
    """ This view gives users the ability to update their bookings"""

    if not request.user.is_authenticated:

        messages.error(request, 'Sorry, you need to be logged in.')

        return redirect(reverse('account_login'))

    # Get booking_id that's pass in by url
    customer = get_object_or_404(Booking, booking_id=booking_id)

    if customer in request.user.customer.all():

        # pass customer as a instance into Customer form
        form = CustomerForm(instance=customer)

        # Check if request equal to POST
        if request.method == 'POST':

            # Pass in the type request and the customer instance
            form = CustomerForm(request.POST, instance=customer)

            # check if the form is valid
            if form.is_valid():

                # save the form
                form.save()

                # Display successful message to user
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your booking has been successfully updated!')

                # Redirect back to booking.html
                return redirect(reverse('bookings:booking'))

        # Pass form into context dictionary
        context = {'form': form}

        # Return and render update-booking.html
        return render(request, 'bookings/update-booking.html', context)

    else:
        messages.error(request, 'Sorry, you are not allow on this page!')

        return redirect(reverse('bookings:index'))


# Delete booking view

@login_required(login_url="account_login")
def delete_booking(request, booking_id):
    """ This view gives users the ability to delete their bookings"""

    if not request.user.is_authenticated:

        messages.error(request, 'Sorry, you need to be logged in.')

        return redirect(reverse('account_login'))

    # Get booking_id that's pass in by url
    customer = get_object_or_404(Booking, booking_id=booking_id)

    if customer in request.user.customer.all():

        # Delete booking_id from database
        customer.delete()

        # Display successful message to user
        messages.add_message(
            request, messages.SUCCESS,
            'Your booking was successfully cancelled!')

        # Redirect back to booking.html
        return redirect(reverse('bookings:booking'))

    else:

        messages.error(request, 'Sorry, you are not allow on this page!')

        return redirect(reverse('bookings:index'))
