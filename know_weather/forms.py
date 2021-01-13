from django import forms

class CityForm(forms.Form):
    City = forms.CharField(max_length=100)

class GeoForm(forms.Form):
    Latitude = forms.CharField(max_length=30) 
    Longitude = forms.CharField(max_length=30) 