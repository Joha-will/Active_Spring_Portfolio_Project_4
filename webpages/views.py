from django.shortcuts import render
from django.views.generic import (TemplateView)


def contact_us(request):
    return render(request, 'webpages/contact-us.html')


class SaunaSteam(TemplateView):
    template_name = 'webpages/sauna-steam.html'
