from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Comment, Order

class UserUpdateFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'from-control',
                'placeholder': 'Email'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'comment-textarea',
                'placeholder': 'Напишите комментарий...'
            }),
        }

class OrderForm(forms.ModelForm):
    delivery_day = forms.DateField(
        widget= forms.DateInput(attrs={'type': 'date'}),
        label="День доставки"
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'delivery_day', 'details']
        widget = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'details': forms.Textarea(attrs={'placeholder': 'Комментарий к заказу', 'rows': 4}),
        }