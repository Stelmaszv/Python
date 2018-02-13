from django import forms
from django.contrib.auth.models import User
from .models import Game
from .validation import expansionIMG
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name','genere','platform','cover']
        name = forms.CharField(validators=[expansionIMG])

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
        }
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
