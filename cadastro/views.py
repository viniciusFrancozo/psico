from django.shortcuts import render, redirect
from .forms import PessoaForm, UsuarioForm, PsicologoForm
from django.contrib.auth import login
from .models import Pessoa, Psicologo
import datetime as dt

# Create your views here.


def index(request):
    user = request.user

    if not Pessoa.objects.filter(pessoa_id=user.id):
        if not Psicologo.objects.filter(psicologo_id=user.id):
            context = {
                'user': user,
                'qs': [],
                'role': 'adm'
            }
        else:
            qs = Psicologo.objects.filter(psicologo_id=user.id)
            context = {
                'user': user,
                'qs': qs,
                'role': 'I'
            }
    else:
        qs = Pessoa.objects.filter(pessoa_id=user.id)
        context = {
            'user': user,
            'qs': qs,
            'role': 'V'
        }
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

#
# def voluntario_cadastro(request):
#     if request.method == 'POST':
#         user_form = UsuarioForm(request.POST)
#         form = PessoaForm(request.POST)
#
#         if user_form.is_valid() and form.is_valid():
#             user = user_form.save()
#
#             pessoa = form.save(commit=False)
#             pessoa.pessoa = user
#
#             pessoa.save()
#
#             login(request, user)
#             return redirect('index')
#
#     else:
#         user_form = UsuarioForm()
#         form = PessoaForm()
#
#     context = {'user_form':user_form, 'form': form}
#     return render(request, 'voluntario_cadastro.html', context)
