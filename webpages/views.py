from django.shortcuts import render
from django.views.generic import (TemplateView)


def index_page(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact-us.html')


class SaunaSteam(TemplateView):
    template_name = 'sauna-steam.html'