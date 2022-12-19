from . import views
from django.urls import path


app_name = 'webpages'


urlpatterns = [
    path('contact-us', views.contact_us, name='contact-us'),
    path('sauna-steam', views.SaunaSteam.as_view(), name='sauna-steam'),
]