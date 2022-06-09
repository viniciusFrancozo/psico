from django.shortcuts import render, redirect
from .forms import PessoaForm, UsuarioForm, PsicologoForm
from django.contrib.auth import login
from .models import Pessoa, Psicologo
import datetime as dt

# Create your views here.


def index(request):
    user = request.user
    context = {'user': user}
    context['mes'] = dt.datetime.now().month
    context['ano'] = dt.datetime.now().year
    print(context)
    return render(request, 'index.html', context)


def cadastro(request):
    user_form = UsuarioForm(request.POST)
    form = PsicologoForm(request.POST)
    form2 = PessoaForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid() and form.is_valid() and form2.is_valid():
            user = user_form.save()
            if user_form.cleaned_data.get('cargo') == 'PI':
                psicologo = form.save(commit=False)
                psicologo.psicologo = user
                psicologo.save()
                login(request, user)
                mes = dt.datetime.now().month
                ano = dt.datetime.now().year
                return redirect('calendario', mes, ano)

            else:
                pessoa = form2.save(commit=False)
                pessoa.pessoa = user
                pessoa.save()

            login(request, user)
            return redirect('index')

    else:
        user_form = UsuarioForm()
        form = PsicologoForm()

    context = {'user_form': user_form, 'form': form}
    return render(request, 'cadastro.html', context)

