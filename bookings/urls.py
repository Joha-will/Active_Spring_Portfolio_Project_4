from . import views

from django.urls import path

app_name = 'bookings'

urlpatterns = [

    # Index page URL

    path('', views.index_page, name='index'),

    # Booking page URL

    path('booking/', views.booking_home, name='booking'),

    # Create booking page URL

    path('create-booking', views.create_booking, name='create'),

    # Update booking page URL

    path('update-booking/<str:booking_id>/', views.update_booking, name='update'),

    # Delete booking URL

    path('delete-booking/<str:booking_id>/', views.delete_booking, name='delete'),

]
