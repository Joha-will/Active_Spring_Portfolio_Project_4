from django.test import TestCase
from .models import Booking

"""
class TestViews(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_booking_home(self):
        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking.html')

    def test_create_booking(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create-booking.html')

    def test_update_booking(self):
        customer = Booking.objects.create(full_name='active-personnel')
        response = self.client.get(f'/update/{booking_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_can_create_booking(self):
        response = self.client.post('/create', {'full_name': 'active-personnel'})
        self.assertRedirects(response, '/booking')

    def test_can_delete_booking(self):
        customer = Booking.objects.create(full_name='active-personnel')
        response = self.client.get(f'/update/{booking_id}')
        self.assertRedirects(response, '/booking')
        current_customers = Booking.objects.filter(id=booking_id)
        self.assertEqual(len(current_customers), 0)
"""