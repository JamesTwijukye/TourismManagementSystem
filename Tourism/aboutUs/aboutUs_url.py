from django.urls import path
from aboutUs.views import WhenView,WhyView,BeforeView


urlpatterns = [
    path('whenToVisit/',WhenView, name='whentovisit'),
    path('whyvisit/', WhyView, name='whyvisit'),
    path('before/', BeforeView ,name = 'beforevisit'), 
]