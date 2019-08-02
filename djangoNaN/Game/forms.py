from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Paris




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class UserParisForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = Paris
        fields = [
            'name',
            'email',
            'montant_paris',
            'equipe',
        ]
