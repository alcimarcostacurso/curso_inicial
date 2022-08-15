import xlwt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from visitantes.forms import VisitanteForm
from visitantes.models import Visitante


@login_required(login_url='login')
def listar_visitante(request):
    visitantes = Visitante.objects.all().order_by('nome')

    paginator = Paginator(visitantes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'visitantes/listar.html', {'page_obj': page_obj})


@login_required(login_url='login')
def persistir_visitante(request, id=None):

    if id:
        instance = get_object_or_404(Visitante, pk=id)
        form = VisitanteForm(request.POST or None, request.FILES or None, instance=instance)
    else:
        instance = None
        form = VisitanteForm(request.POST or None, request.FILES or None, instance=None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            if instance:
                messages.success(request, 'Visitante atualizado com sucesso!')
            else:
                messages.success(request, 'Visitante salvo com sucesso!')
            return redirect('visitantes:listar')

    context = {
        'form': form,
        'visitante': instance
    }

    return render(request, 'visitantes/persistir-visitante.html', context)


@login_required(login_url='login')
def deletar_visitante(request, id):
    visitante = get_object_or_404(Visitante, pk=id)

    if request.method == 'POST':
        if visitante:
            visitante.delete()
            messages.success(request, 'Visitante removido com sucesso!!!')
            return redirect('visitantes:listar')

    context = {
        'visitante': visitante
    }

    return render(request, 'visitantes/deletar.html', context)


@login_required(login_url='login')
def lista_de_visitantes_ajax(request):

    term = request.GET.get('term')
    visitantes = Visitante.objects.filter(nome__icontains=term)
    response_content = list(visitantes.values())
    return JsonResponse(response_content, safe=False)


@login_required(login_url='login')
def detalhar_visitante(request, id):
    visitante = get_object_or_404(Visitante, pk=id)

    acessos = visitante.controleacesso_set.all()
    print(acessos)

    context = {
        'visitante': visitante,
        'acessos': acessos
    }

    return render(request, 'visitantes/detalhar.html', context)


class VisitanteExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="visitantes.xls"'
        wb = xlwt.Workbook(encoding='utf_8')
        ws = wb.add_sheet('Visitantes')

        row_num = 0
        columns = ['Nome', 'CPF', 'Sexo', 'Telefone', 'Data de nascimento']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        visitantes = Visitante.objects.all()

        row_num = 1
        for visitante in visitantes:
            ws.write(row_num, 0, visitante.nome)
            ws.write(row_num, 1, visitante.cpf)
            ws.write(row_num, 2, visitante.sexo)
            ws.write(row_num, 3, visitante.telefone)
            ws.write(row_num, 4, visitante.data_nascimento)
            row_num += 1

        wb.save(response)
        return response
