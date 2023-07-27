from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistration
#         # fields = ['username', 'email', 'password1', 'password2']
#         fields = '__all__'


class OrderForm (forms.ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        # fields = ('user', 'product', 'status')
        fields = ['user', 'product', 'status']

        labels = {
        }

        widgets = {
            'user': forms.Select(attrs={'class':'form-select mb-3 mt-2'}),
            'product': forms.Select(attrs={'class':'form-select mb-2 mt-2'}),
            'status': forms.Select(attrs={'class':'form-select mb-2 mt-2'}),
        }
