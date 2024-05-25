from django.contrib import admin

# Register your models here.

from booking.models import Hotel,Booking,FeaturedDestination,HomeImages
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(FeaturedDestination)
admin.site.register(HomeImages)

