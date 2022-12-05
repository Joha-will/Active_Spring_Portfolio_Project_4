from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('booking_id', 'booked_on', 'no_of_persons')
    list_display = ('booking_id', 'full_name', 'no_of_persons', 'approved', 'booked_on')
    search_fields = ('full_name', 'email')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
