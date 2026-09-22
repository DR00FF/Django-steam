from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User

from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'

    }))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите почту'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": ""}))
    banner = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}),required=False,label="Шапка профиля (2048×1152)")
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        "readonly": True
    }))


    class Meta:
        model = User
        fields = ['username','image','email', 'banner']

