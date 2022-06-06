from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .utils import Calendar
from cadastro.models import Account, Psicologo, Pessoa
from consultar.models import Consulta
from consultar.forms import ConsultaForm
import datetime


# Create your views here.

def calendario(request, mes, ano):
    if request.user.cargo == 'PE':
        cal = Calendar(ano, mes, request.user)
        html_cal = cal.formatmonth(withyear=True)
        context = {
            'cal': html_cal,
            'mes': mes,
            'ano': ano,
            'dias': '',
            'aux': 0
        }
        dias = Consulta.objects.filter(data__month=datetime.datetime.now().month,
                                       data__year=datetime.datetime.now().year)
        context['dias'] = dias
        return render(request, 'agenda.html', context)
    else:
        cal = Calendar(ano, mes, request.user)
        html_cal = cal.formatmonth(withyear=True)
        context = {
            'cal': html_cal,
            'mes': mes,
            'ano': ano,
            'dias': '',
            'aux': 0
        }
        dias = Consulta.objects.filter(data__month=datetime.datetime.now().month,
                                       data__year=datetime.datetime.now().year)
        context['dias'] = dias
        return render(request, 'agenda.html', context)

def calendario_visualizar(request, mes, ano, dia):
    user = request.user
    nomes = []
    consulta = get_list_or_404(Consulta, data__month=mes, data__day=dia, data__year=ano)
    print(consulta)
    for i in consulta:
        nomes.append(Account.objects.get(pessoa=i.cliente_id))
        print(nomes)
    if request.method == 'POST':
        if user.cargo == 'PE':
            nova_data = []
            novo_horario = []
            for i in request.POST.getlist('data'):
                a = datetime.datetime.strptime(i, '%d/%m/%Y')
                nova_data.append(a)
            for i in request.POST.getlist('horario'):
                novo_horario.append(i)

            for i, x, y in zip(novo_horario, nova_data, consulta):
                y.horario = i
                y.data = x
                y.save(update_fields=['horario','data'])
            return redirect('index')
        else:
            pessoas = zip(consulta, nomes)
            context = {'consulta': pessoas, 'user':user}

    else:
        if user.cargo == 'PE':

            print(consulta)
            context = {'consulta': consulta, 'user':user}
        else:
            pessoas = zip(consulta, nomes)
            context = {'consulta': pessoas, 'user': user}

    return render(request, 'cal_visualizar.html', context)
