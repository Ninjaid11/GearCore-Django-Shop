from allauth.core.ratelimit import clear
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вашу почту'
        })
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                self.user = authenticate(username=user.username, password=password)
                if self.user is None:
                    raise forms.ValidationError('Неверный email или пароль')
            except User.DoesNotExist:
                raise forms.ValidationError('Пользователь с такой почтой не найден')
        return cleaned_data

    def get_user(self):
        return self.user
