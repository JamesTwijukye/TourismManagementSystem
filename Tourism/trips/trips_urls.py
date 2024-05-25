from django.urls import path
from trips.views import TripsView



urlpatterns = [
    path('', TripsView,name='trips'),
]
