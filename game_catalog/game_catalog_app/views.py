from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Game, Comment
from .forms import GameForm, CommentForm, RegisterForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Game Catalog'})
    else:
        return redirect('game_catalog_app:games')


@login_required
def comment(req, id):
    if req.method == 'POST':
        form = CommentForm(req.POST)

        if form.is_valid():
            print('valid AF')
            game = Game.objects.get(id=id)
            a = Comment(content=form.cleaned_data['content'], author=req.user, game=game)
            a.save()

    return redirect('game_catalog_app:games')

@login_required
def games(req):
    tmp = Game.objects.all()
    return render(req, 'games.html', {'games': tmp})


@login_required
def game(req, id):
    game = get_object_or_404(Game, id=id)
    comments = []
    comment_form = CommentForm()
    try:
        comments = get_list_or_404(Comment, game=game)
    except Exception:
        pass
    return render(req, 'game.html', {'game': game, 'comments': comments, 'comment_form': comment_form, 'page_title': game.title})


@permission_required('game_catalog_app.change_game')
def edit(req, id):
    if req.method == 'POST':
        form = GameForm(req.POST)

        if form.is_valid():
            a = Game.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.description = form.cleaned_data['description']
            a.price = form.cleaned_data['price']
            a.rating = form.cleaned_data['rating']
            a.save()
            return redirect('game_catalog_app:games')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Game.objects.get(id=id)
        form = GameForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('game_catalog_app.add_game')
def new(req):
    if req.method == 'POST':
        form = GameForm(req.POST)

        if form.is_valid():
            a = Game(title=form.cleaned_data['title'], description=form.cleaned_data['description'],
                     price=form.cleaned_data['price'], rating=form.cleaned_data['rating'])
            a.save()
            return redirect('game_catalog_app:games')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = GameForm()
        return render(req, 'new.html', {'form': form})

def register(req):
    if req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Game Catalog'})
    if req.method == "POST":
        form = RegisterForm(req.POST or None)

        if form.is_valid():
            user = form.save()
            return render(req, 'index.html', {'page_title': 'Game Catalog'})
    else:
        form = RegisterForm()
    return render(req, '../templates/registration/register.html', { 'form': form })