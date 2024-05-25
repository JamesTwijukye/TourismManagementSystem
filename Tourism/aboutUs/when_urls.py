from django.urls import path
from aboutUs.views import WhenView
urlpatterns = [
    path('', WhenView,name='when'),

]