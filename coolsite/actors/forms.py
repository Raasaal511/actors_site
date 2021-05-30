from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Actor, Category

from captcha.fields import CaptchaField


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Actor
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})

        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 250:
            print(title, 'error')
            raise ValidationError('Длина привыщает 250 символов')

        print(title, 'no error')


class RegisterUserForm(UserCreationForm):
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-input'}),
        'email': forms.EmailInput(attrs={'class': 'form-input'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
    }

    username = forms.CharField(label='Логин', widget=widgets['username'])
    email = forms.CharField(label='Email', widget=widgets['email'])
    password1 = forms.CharField(label='Пароль', widget=widgets['password1'])
    password2 = forms.CharField(label='Повтор пароля', widget=widgets['password2'])

    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-input'}),
        'password': forms.PasswordInput(attrs={'class': 'form-input'}),
    }

    username = forms.CharField(label='Логин', widget=widgets['username'])
    password = forms.CharField(label='Пароль', widget=widgets['password'])


class ContactForm(forms.Form):

    widgets = {
        'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
    }

    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=widgets['content'])
    captcha = CaptchaField()
