from django import forms
from django.contrib.auth.models import User
from .models import Game
from django.core.exceptions import ValidationError
from .models import Game,MyLibrary,Platform
from django.shortcuts import get_object_or_404
class GameForm(forms.ModelForm):
    class Meta:
        GameDetils = get_object_or_404(Game, pk=23)
        model = Game
        fields = ['name','genere','platform','cover']
        widgets = {
            'name': forms.TextInput(attrs={'value':GameDetils.name,'placeholder':'podaj nazwę gry'}),
            'genere': forms.TextInput(attrs={'value':GameDetils.genere,'placeholder':'podaj gatunek'}),
        }

        labels = {
            'name': 'Nazwa Gry',
            'genere': 'Gatunek',
            'platform':'Platforma',
            'cover'   :'Okładka'
        }
        help_texts = {
            'name': 'Podaj Nazwe Gry',
        }
        error_messages = {
            'name': {
                'max_length': 'za duzo znaków',
            },
            'genere':{
                'max_length': 'za duzo znaków',
            },
            'cover':{
                'img':'złe roszerzenie'
            }
        }
    def GetID(ID):
        return ID


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
