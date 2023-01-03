from . import views

from django.urls import path

app_name = 'bookings'

urlpatterns = [

    path('', views.index_page, name='index'),

    path('booking/', views.booking_home, name='booking'),

    path('create-booking', views.create_booking, name='create'),

    path('update-booking/<str:booking_id>/', views.update_booking, name='update'),

    path('delete-booking/<str:booking_id>/', views.delete_booking, name='delete'),
    
]
