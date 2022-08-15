import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from controle_acessos.forms import ControleAcessoForm, ControleAcessoEditForm
from controle_acessos.models import ControleAcesso


@login_required(login_url='login')
def listar_acessos(request):

    search = request.GET.get('search', None)

    acessos = ControleAcesso.objects.all().order_by('-data_entrada', '-hora_entrada')

    if search:
        acessos = ControleAcesso.objects.filter(Q(visitante__nome__icontains=search) |
                                                Q(visitante__cpf__icontains=search))\
            .order_by('-data_entrada', '-hora_entrada')

    paginator = Paginator(acessos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'controle_acessos/listar.html', context)


@login_required(login_url='login')
def criar_acessos(request):
    form = ControleAcessoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.user = request.user
            form_temp.save()
            form.save_m2m()
            messages.success(request, 'Acesso cadastrado com sucesso!')
            return redirect('controle_acessos:listar')

    context = {
        'form': form
    }

    return render(request, 'controle_acessos/criar.html', context)


@login_required(login_url='login')
def editar_acesso(request, id):
    acesso = get_object_or_404(ControleAcesso, pk=id)

    form = ControleAcessoEditForm(request.POST or None, instance=acesso)

    if request.method == 'POST':
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.user = request.user
            form_temp.save()
            form.save_m2m()
            messages.success(request, 'Acesso editado com sucesso!')
            return redirect('controle_acessos:listar')

    context = {
        'form': form
    }

    return render(request, 'controle_acessos/editar.html', context)


@login_required(login_url='login')
def deletar_acesso(request, id):
    acesso = get_object_or_404(ControleAcesso, pk=id)

    if request.method == 'POST':
        acesso.delete()
        messages.success(request, 'Acesso removido com sucesso!!')
        return redirect('controle_acessos:listar')

    return render(request, 'controle_acessos/deletar.html')


@login_required(login_url='login')
def registrar_saida(request, id):
    acesso = get_object_or_404(ControleAcesso, pk=id)
    data_atual = datetime.datetime.now()
    hora_atual = datetime.datetime.now().time()

    if request.method == 'POST':
        acesso.data_saida = data_atual
        acesso.hora_saida = hora_atual
        acesso.save()
        messages.success(request, 'Saída registrada com sucesso!!')
        return redirect('controle_acessos:listar')


