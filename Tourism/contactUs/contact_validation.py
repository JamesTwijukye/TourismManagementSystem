from django import forms

class ContactForm(forms.Form):
    fullname  = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    phone = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=200)
