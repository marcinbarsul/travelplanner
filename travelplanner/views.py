
from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Hotel



def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            visa_duration = data['visa_duration']
            visa_price = data['visa_price']

            if not isinstance(visa_duration, int) or visa_duration <= 0:
                form.add_error('visa_duration', 'Wprowadź dodatnią liczbę całkowitą dla długości wizy.')
            if not isinstance(visa_price, (int, float)) or int(visa_price) != visa_price or visa_price <= 0:
                form.add_error('visa_price', 'Wprowadź liczbę całkowitą lub zmiennoprzecinkową dla ceny wizy.')

            if form.is_valid():
                flight = form.save()
                return redirect('flight_list')
    else:
        form = FlightForm()

    return render(request, 'create_flight.html', {'form': form})

def travel_costs(request):
    hotels = Hotel.objects.all()

    total_hotel_cost = sum(hotel.cena for hotel in hotels)

    context = {
        'hotels': hotels,
        'total_hotel_cost': total_hotel_cost,
    }

    return render(request, 'your_template.html', context)