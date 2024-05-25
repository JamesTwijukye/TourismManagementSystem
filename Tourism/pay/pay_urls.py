from django.urls import path
from pay.views import PayView, submit_pay_formView
from .views import view_html_report
from .views import PayView, submit_pay_formView, view_html_report

urlpatterns = [
    path("", PayView, name="pay"),
    path("submit_pay_form", submit_pay_formView, name="submit_pay_form"),
    path("payreport/", view_html_report, name="pay_report"),
    path("payreport/", view_html_report, name="pay_report"),  # Add this line
]
