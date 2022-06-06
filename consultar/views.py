from django.shortcuts import render, redirect
from .forms import ConsultaForm
from cadastro.models import Pessoa, Psicologo, Account

# Create your views here.

def consultar(request):
    user = request.user
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            print(Pessoa.objects.filter(pessoa_id=user.id))
            new_form = form.save(commit=False)
            print(new_form.cliente_id)
            new_form.cliente_id = Pessoa.objects.filter(pessoa_id=user.id)[0]
            print(new_form.cliente_id)
            new_form.save()
            return redirect('index')
    else:
        form = ConsultaForm()

    return render(request, 'consultar.html', {'form': form})
