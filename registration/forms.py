from django import forms


class RegistrationFrom(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    phone_number = forms.CharField(required=True, widget=forms.TextInput())
