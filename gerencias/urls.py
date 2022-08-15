from django.urls import path

from gerencias.views import listar_gerencia, persistir_gerencia, deletar_gerencia

app_name = 'gerencias'

urlpatterns = [
    path('listar/', listar_gerencia, name='listar'),
    path('persistir/', persistir_gerencia, name='persistir'),
    path('persistir/<int:id>/', persistir_gerencia, name='editar'),
    path('deletar/<int:id>/', deletar_gerencia, name='deletar')
]