from django import forms


class RegistrationFrom(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(), label='Имя')
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Пароль')
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    phone_number = forms.CharField(required=False, widget=forms.TextInput(), label='Телефон')
