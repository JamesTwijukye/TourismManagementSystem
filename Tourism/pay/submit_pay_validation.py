from django import forms

class PayForm(forms.Form):
    price = forms.CharField()
    services = forms.CharField(max_length=100)
    cardholder = forms.CharField(max_length=100)

    number_of_adults = forms.CharField(max_length=100)
    number_of_children = forms.CharField(max_length=100)
    personal_name = forms.CharField(max_length=100)
    personal_mobile = forms.CharField(max_length=100)
    personal_nin = forms.CharField(max_length=100)
