from django.forms import ModelForm, EmailInput, NumberInput
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
            'email': EmailInput(attrs={
                'placeholder': 'Email'}),
            'phone_number': NumberInput(attrs={
                'placeholder': '+44XXXXXXXXXX'
            })
        }
