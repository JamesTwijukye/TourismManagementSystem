from django.urls import path
from aboutUs.views import WhyView
urlpatterns = [
    path('',WhyView,name='why'),

]