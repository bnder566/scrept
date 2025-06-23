from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser

# نموذج التسجيل
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="اسم المستخدم",
        widget=forms.TextInput(attrs={
            'oninput': "checkUsernameAvailability(this.value);"
        })
    )
    phone_number = forms.CharField(
        label="رقم الجوال",
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'مثال: 0501234567',
            'pattern': r'^05\d{8}$',
            'title': 'رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام'
        })
    )

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

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.startswith('05') or len(phone) != 10:
            raise forms.ValidationError("رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام")
        return phone

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم غير متاح")
        return username

# نموذج تسجيل الدخول
class UserLoginForm(forms.Form):
    identifier = forms.CharField(label="اسم المستخدم أو رقم الجوال")
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')

        if identifier and password:
            try:
                # تحقق هل هو رقم جوال أو اسم مستخدم
                user = CustomUser.objects.get(phone_number=identifier)
                username = user.username
            except CustomUser.DoesNotExist:
                username = identifier  # قد يكون اسم مستخدم

            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("بيانات الدخول غير صحيحة")
            self.user = user
        return cleaned_data
