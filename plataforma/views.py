from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect 
from django.contrib.auth.models import User
from .models import Nota

# Create your views here.


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user:
            login(request, user)

        return redirect('plataforma')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    username = request.POST.get('username')
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirmesenha = request.POST.get('confirme-senha')

    if User.objects.filter(username=username):
        return HttpResponse('Já existe um usuário com esse login!')
    
    if senha != confirmesenha:
        return HttpResponse('As senhas não batem!')

    user = User.objects.create_user(username, email, password=senha, first_name=nome)
    user.save()
    return redirect('plataforma')


def logout_view(request):
    logout(request)
    return redirect('plataforma')


@login_required(login_url='logar')
def plataforma(request):
    username = request.user
    notas = Nota.objects.filter().order_by('-id')
    context = {"notas": notas, 'logado': True, 'username': username}
    return render(request, 'plataforma.html', context)


@login_required(login_url='logar')
def cadastro_nota(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        corpo = request.POST.get('corpo')
        username = request.user

        nota = Nota.objects.create(
            titulo=titulo, username=username, corpo=corpo)
        nota.save()
        return redirect('plataforma')
