from django import forms

class SignUpForm(forms.Form):
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
