from django.urls import path
from .views import (listar_visitante, persistir_visitante, deletar_visitante, lista_de_visitantes_ajax,
                    detalhar_visitante, VisitanteExcel)

app_name = 'visitantes'

urlpatterns = [
    # path('ajax/select/setores/', setores_por_gerencia, name='setores_ajax'),
    path('listar/', listar_visitante, name='listar'),
    path('persistir/', persistir_visitante, name='persistir'),
    path('persistir/<int:id>/', persistir_visitante, name='editar'),
    path('deletar/<int:id>/', deletar_visitante, name='deletar'),
    path('detalhar/<int:id>/', detalhar_visitante, name='detalhar'),
    path('ajax/lista/visitantes/', lista_de_visitantes_ajax, name='lista_de_visitantes_ajax'),
    path('imprimir/', VisitanteExcel.as_view(), name='visitantes_excel')
]