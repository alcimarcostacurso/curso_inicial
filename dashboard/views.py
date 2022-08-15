from datetime import datetime
from io import BytesIO

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa

from controle_acessos.models import ControleAcesso


@login_required(login_url='login')
def dashboard(request):
    # dados da quantidade de visita por setores
    labels_setores = []
    data_setores = []

    labels_por_sexo = []
    data_por_sexo = []

    acessos_por_setores = ControleAcesso.objects.all().values('setores__nome').\
        order_by().annotate(quantidade=Count('id')).values_list('setores__nome', 'quantidade')
    acessos_por_sexo = (ControleAcesso.objects.all().values('visitante__sexo').
                        annotate(quantidade=Count('id'))).values_list('visitante__sexo', 'quantidade')

    for acesso in acessos_por_setores:
        labels_setores.append((acesso[0]))
        data_setores.append((acesso[1]))

    for acesso in acessos_por_sexo:
        labels_por_sexo.append((acesso[0]))
        data_por_sexo.append((acesso[1]))

    print(labels_por_sexo)
    print(data_por_sexo)

    context = {
        'labels_setores': labels_setores,
        'data_setores': data_setores,
        'labels_por_sexo': labels_por_sexo,
        'data_por_sexo': data_por_sexo
    }
    return render(request, 'dashboard/dashboard.html', context)


def relatorio(request):

    return render(request, 'dashboard/relatorio.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def exportar_pdf(request):
    acessos = []

    data_inicio_pdf = datetime.now()
    data_fim_pdf = datetime.now()

    data_inicio = request.GET.get('data_inicio', None)
    data_fim = request.GET.get('data_fim', None)

    if data_inicio and data_fim:
        data_inicio_pdf = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim_pdf = datetime.strptime(data_fim, '%Y-%m-%d').date()
        acessos = ControleAcesso.objects.filter(data_entrada__range=[data_inicio, data_fim]).\
            select_related('visitante')


    data = {
        'acessos': acessos,
        'data_inicio_pdf': data_inicio_pdf,
        'data_fim_pdf': data_fim_pdf
    }

    pdf = render_to_pdf('pdf/pdf_acessos.html', data)
    return HttpResponse(pdf, content_type='application/pdf')



