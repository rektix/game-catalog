from django.forms import ModelForm, Form
import django.forms as f
from .models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'rating']

