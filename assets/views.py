from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import  render, redirect, get_object_or_404
from django.template import loader
from .models import Game,MyLibrary,Platform
from .forms import GameForm, UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import Permission, User
from django.db import IntegrityError

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def index(request):
    Games = Game.objects.all()
    Platforms=Platform.objects.all()
    MylibaryCount=MyLibrary.objects.filter(user=request.user)
    LibaryCount=MylibaryCount.count()
    return render(request,'index.html',{'Platforms':Platforms,'Games':Games,'LibaryCount':LibaryCount })
def ShowGame(request,Game_id):
    try:
        Games = Game.objects.get(pk=Game_id)
    except Games.DoestNotExist:
        raise Http404("Wybrna Gra nie istnienie ")
    Inlabrary= 0
    game=MyLibrary.objects.filter(game=Game_id)
    if game:
        Inlabrary=1
    context = {
        'Game'     :Games,
        'Inlabrary':Inlabrary,
    }
    return render(request,'ShowGame.html',context)
def Create(request):
    Games = Game.objects.all()
    form = GameForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        context = {
                'form': form,
                'massage': 'Zdjęcie musi być w formacie'
        }
        Game.objects.create(name=request.POST['name'], genere=request.POST['genere'], cover=request.FILES['cover'],platform=get_object_or_404(Platform, pk=request.POST['platform']))
        return redirect('/')
    return render(request, 'Create.html',context)
def EditGame(request,Game_id):
    try:
        Games = Game.objects.get(pk=Game_id)
    except Games.DoestNotExist:
        raise Http404("Wybrna Gra nie istnienie ")
    form = GameForm(request.POST or None, request.FILES or None)
    context = {
        'Game': Games,
        'form': form
    }
    if form.is_valid():
        context = {
            'Game': Games,
            'form': form,
            'massage': 'Zmiany Zapisane'
        }
        Games.name = request.POST['name'];
        Games.genere = request.POST['genere'];
        Games.save()
    return render(request,'Edit.html',context)
def Dalete(request,Game_id):
    try:
        Games = Game.objects.get(pk=Game_id)
    except Games.DoestNotExist:
        raise Http404("Wybrna Gra nie istnienie ")
    Games.delete()
    return redirect('/')
def Register(request):
    form = UserForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
        context = {
            "form": form,
        }
    return render(request, 'Edit.html', context)
def logoutUser(request):
    logout(request)
    return redirect('/')
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')
def MyLibraryView(request):
    Library = MyLibrary.objects.filter(user=request.user)
    context = {
        'Library': Library
    }
    return render(request, 'library.html',context)
def MyLibraryAction(request,Game_id):
    ML=MyLibrary()
    ML.game=get_object_or_404(Game, pk=Game_id)
    ML.user=request.user
    ML.save()
    return redirect('/MyLibrary')
def ItemRemuveAction(request,Game_id):
    game=get_object_or_404(MyLibrary, pk=Game_id)
    game.delete()
    return redirect('/MyLibrary')
