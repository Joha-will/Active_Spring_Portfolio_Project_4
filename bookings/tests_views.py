from django.test import TestCase
from .models import Booking

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
        customer = Booking.objects.create(full_name='active-personel')
        response = self.client.get(f'/update/{booking_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_delete_booking(self):
    def test_can_create_booking(self):
    def test_can_update_booking(self):
    def test_can_delete_booking(self):