from django.urls import path

from booking.views import BookingView, BookNowView

urlpatterns = [

    path('',BookingView,name='booking'),
    path('booknow',BookNowView,name='booknow')
] 