from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    path = settings.BUS_STATION_CSV

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        station_list = list(reader)

    paginator = Paginator(station_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
