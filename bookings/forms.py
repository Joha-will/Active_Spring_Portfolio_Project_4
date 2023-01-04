from django.forms import ModelForm, EmailInput, NumberInput, TextInput

from django import forms

from bookings.models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = '__all__'

        exclude = ['booked_on', 'approved', 'booking_status', 'user']

        widgets = {
            'booking_date': DateInput(),
            'email': EmailInput(attrs={
                'placeholder': 'Email'}),
            'phone_number': NumberInput(attrs={
                'placeholder': '+44XXXXXXXXXX'
            }),
            'name': TextInput(attrs={
                'placeholder': 'Full Name'
            }),
        }
