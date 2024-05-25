from django.urls import path
from aboutUs.views import BeforeView
urlpatterns = [
    path('', BeforeView,name='before'),
]