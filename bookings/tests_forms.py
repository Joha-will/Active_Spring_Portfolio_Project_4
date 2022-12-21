from django.test import TestCase
from bookings.forms import CustomerForm


class TestCustomerForm(TestCase):

    def test_fullname_field_is_required(self):
        form = CustomerForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_form_has_required_fields(self):
        form = CustomerForm()
        self.assertEqual(form.Meta.exclude, ['booked_on', 'approved'])
