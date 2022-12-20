from django.forms import ModelForm
from django import forms
from bookings.models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['booked_on', 'approved', 'booking_status']
        widgets = {
            'booking_date': DateInput(),
        }
