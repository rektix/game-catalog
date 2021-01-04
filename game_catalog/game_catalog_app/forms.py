from django.forms import ModelForm, Form
import django.forms as f
from .models import Game, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'rating']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
