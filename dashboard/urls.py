from django.urls import path
from .views import dashboard, relatorio, exportar_pdf

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('relatorio/', relatorio, name='relatorio'),
    path('relatorio/acessos/pdf/', exportar_pdf, name='exportar_pdf')
]