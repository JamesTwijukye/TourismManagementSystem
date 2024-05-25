from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from booking .models import FeaturedDestination,HomeImages



# Create your views here.
def HomeView(request):
    dest_items = FeaturedDestination.objects.all()
    hm_items =HomeImages.objects.all()

    return render(request, 'home.html', {"items":dest_items,"images":hm_items})
