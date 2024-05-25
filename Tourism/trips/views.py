from django.shortcuts import render
from trips.models import Trip
# Create your views here.
def TripsView(request):

    trip_items = Trip.objects.all()


    return render(request, 'trips.html', {"trips":trip_items})

