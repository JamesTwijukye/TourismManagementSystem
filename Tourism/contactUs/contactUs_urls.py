from django.urls import path
from contactUs.views import ContactView, submit_contact_formView, view_contact_report
urlpatterns = [
    path('', ContactView,name='contact'),
    path('submit_contact_form', submit_contact_formView,name='submit_contact_form'),
    path('contactReport/', view_contact_report, name='contact_report'),  # URL for viewing the contact report

]