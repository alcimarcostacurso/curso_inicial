from django.urls import path

from controle_acessos.views import (listar_acessos,
                                    criar_acessos,
                                    editar_acesso,
                                    deletar_acesso,
                                    registrar_saida)

app_name = 'controle_acessos'

urlpatterns = [
    path('listar/', listar_acessos, name='listar'),
    path('criar/', criar_acessos, name='criar'),
    path('editar/<int:id>/', editar_acesso, name='editar'),
    path('deletar/<int:id>/', deletar_acesso, name='deletar'),
    path('registrar-saida/<int:id>/', registrar_saida, name='registrar_saida'),
]