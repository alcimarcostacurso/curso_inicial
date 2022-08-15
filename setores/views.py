from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from setores.forms import SetorForm
from setores.models import Setor


@login_required(login_url='login')
def setores_por_gerencia(request):
    gerencia_id = request.GET.get('gerencia')

    setores = Setor.objects.filter(gerencia__id=gerencia_id)

    return render(request, 'setores/setores-select-options.html', {'setores': setores})


@login_required(login_url='login')
def listar_setor(request):
    setores = Setor.objects.all().order_by('nome')

    paginator = Paginator(setores, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'setores/listar.html', {'page_obj': page_obj})


@login_required(login_url='login')
@permission_required(['setor.add_setor', 'setor.change_setor'], raise_exception=True)
def persistir_setor(request, id=None):

    if id:
        instance = get_object_or_404(Setor, pk=id)
        form = SetorForm(request.POST or None, instance=instance)
    else:
        instance = None
        form = SetorForm(request.POST or None, instance=None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            if instance:
                messages.success(request, 'Setor atualizado com sucesso!')
            else:
                messages.success(request, 'Setor salvo com sucesso!')
            return redirect('setores:listar')

    context = {
        'form': form,
        'setor': instance
    }

    return render(request, 'setores/persistir-setor.html', context)


@login_required(login_url='login')
@permission_required('setor.deletar_setor', raise_exception=True)
def deletar_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)

    if request.method == 'POST':
        if setor:
            setor.delete()
            messages.success(request, 'Setor removido com sucesso!!!')
            return redirect('setores:listar')

    context = {
        'setor': setor
    }

    return render(request, 'setores/deletar.html', context)


@login_required(login_url='login')
def lista_de_setores_ajax(request):

    term = request.GET.get('term')
    setores = Setor.objects.filter(nome__icontains=term)
    response_content = list(setores.values())
    return JsonResponse(response_content, safe=False)