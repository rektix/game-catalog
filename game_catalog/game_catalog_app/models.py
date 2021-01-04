from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=1, validators=[
            MinValueValidator(1)
        ])
    rating = models.IntegerField(default=1, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
