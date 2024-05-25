from django import forms

class BookNowForm(forms.Form):
    hotel_price = forms.IntegerField()
    number_of_adults = forms.IntegerField()
    number_of_children = forms.IntegerField()
    number_of_rooms = forms.IntegerField()

    personal_name = forms.CharField(max_length=100)
    personal_mobile = forms.CharField(max_length=100)
    personal_nin = forms.CharField(max_length=100)
