from django import forms


class RegistrationFrom(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    phone_number = forms.CharField(required=False, widget=forms.TextInput())
