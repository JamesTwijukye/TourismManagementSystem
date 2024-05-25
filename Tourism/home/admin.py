from django.contrib import admin # type: ignore

# Register your models here.
from home.models import User
from trips.models import Trip
admin.site.register(User)

admin.site.register(Trip)