from django.forms import ModelForm, Form
import django.forms as f
from .models import Game, Comment


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']