from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    "The booking model"
    booking_id = models.AutoField(primary_key=True)
    full_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer')
    email = models.EmailField(max_length=254)
    no_of_persons = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return str(self.full_name)