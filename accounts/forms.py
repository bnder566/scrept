from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'is_collector', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم',
            'phone_number': 'رقم الجوال',
            'is_collector': 'هل أنت مشتري؟',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="اسم المستخدم")
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput)
