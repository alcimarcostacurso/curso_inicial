from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from gerencias.forms import GerenciaForm
from gerencias.models import Gerencia


@login_required(login_url='login')
def listar_gerencia(request):
    gerencias = Gerencia.objects.all().order_by('nome')

    paginator = Paginator(gerencias, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gerencias/listar.html', {'page_obj': page_obj})


@login_required(login_url='login')
@permission_required(['gerencia.add_gerencia', 'gerencia.change_gerencia'], raise_exception=True)
def persistir_gerencia(request, id=None):

    if id:
        instance = get_object_or_404(Gerencia, pk=id)
        form = GerenciaForm(request.POST or None, instance=instance)
    else:
        instance = None
        form = GerenciaForm(request.POST or None, instance=None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            if instance:
                messages.success(request, 'Gerência atualizada com sucesso!')
            else:
                messages.success(request, 'Gerência salva com sucesso!')
            return redirect('gerencias:listar')

    context = {
        'form': form,
        'gerencia': instance
    }

    return render(request, 'gerencias/persistir-gerencia.html', context)


@login_required(login_url='login')
@permission_required('gerencia.delete_gerencia', raise_exception=True)
def deletar_gerencia(request, id):
    gerencia = get_object_or_404(Gerencia, pk=id)

    if request.method == 'POST':
        if gerencia:
            gerencia.delete()
            messages.success(request, 'Gerência removida com sucesso!!!')
            return redirect('gerencias:listar')

    context = {
        'gerencia': gerencia
    }

    return render(request, 'gerencias/deletar.html', context)
