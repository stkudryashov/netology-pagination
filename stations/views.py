from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from django.urls import reverse

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    result = list()

    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)

    paginator = Paginator(result, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
