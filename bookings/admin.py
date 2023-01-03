from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_filter = ('booking_id', 'booked_on', 'no_of_persons')

    list_display = (
        'booking_id', 'user', 'no_of_persons',
        'approved', 'booked_on', 'booking_status')

    search_fields = ('user', 'email')
    
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
