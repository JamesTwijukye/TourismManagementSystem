from django.urls import path
from home.views import HomeView
urlpatterns = [
    path('', HomeView ,name='home'),

]