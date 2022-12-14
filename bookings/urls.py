from . import views
from django.urls import path

app_name = 'bookings'

urlpatterns = [
    path('booking', views.booking_home, name='booking'),
    path('create-booking/', views.create_booking, name='create'),
    path('update-booking/<str:pk>/', views.update_booking, name='update-booking'),
]