from django.urls import path

from setores.views import setores_por_gerencia, listar_setor, persistir_setor, deletar_setor, lista_de_setores_ajax

app_name = 'setores'

urlpatterns = [
    path('ajax/select/setores/', setores_por_gerencia, name='setores_ajax'),
    path('listar/', listar_setor, name='listar'),
    path('persistir/', persistir_setor, name='persistir'),
    path('persistir/<int:id>/', persistir_setor, name='editar'),
    path('deletar/<int:id>/', deletar_setor, name='deletar'),
    path('ajax/listar/setores', lista_de_setores_ajax, name='lista_de_setores_ajax')
]