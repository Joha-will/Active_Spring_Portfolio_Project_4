from django.db import models
from django.contrib.auth.models import User
import datetime


class Booking(models.Model):
    "The booking model"
    booking_id = models.AutoField(primary_key=True)
    full_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer', null=True)
    email = models.EmailField(max_length=254)
    no_of_persons = models.IntegerField(default=0)
    booking_date = models.DateField(default=datetime.date.today)
    booking_time = models.CharField(max_length=10, default='08:00')
    phone_number = models.CharField(max_length=20)
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return str(self.full_name)