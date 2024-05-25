from django.urls import path
from loginA.views import SignupAuth, SignupView

urlpatterns = [
    
    path('', SignupView,name='signup'),
     path('signupauth', SignupAuth,name='signupauth'),

   ]