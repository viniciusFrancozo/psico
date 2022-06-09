from django.shortcuts import render,redirect
from .models import Remedio, Receita
from cadastro.models import Pessoa
from .forms import ReceitaForm, RemedioForm
# Create your views here.




# Create your views here.


def receita_view(request):
    user = request.user
    remedio = Remedio.objects.all()
    paciente = Pessoa.objects.all()
    # p1 =
    # a1 = Receita(remedio=, quantidade=, data_fim=, paciente=,)
    # a1.publications.add(p1)
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            return redirect('index')
    else:
        form = ReceitaForm()
    ctx = {'remedio': remedio,
           'paciente': paciente,
           'form': form}

    return render(request, "receita.html", ctx)

def cadastrar_remedio(request):
    if request.method == 'POST':
        form = RemedioForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            return redirect('index')
    else:
        form = RemedioForm()
    ctx = {'form':form}
    return render(request, 'cadastrar_remedio.html', ctx)
