from . import views
from django.urls import path


app_name = 'webpages'


urlpatterns = [
    # Contact Us URL

    path('contact-us/', views.contact_us, name='contact-us'),

    # Sauna Steam URL

    path('sauna-steam/', views.SaunaSteam.as_view(), name='sauna-steam'),
    
]
