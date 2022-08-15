from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, listar_usuarios, edit_user_funcionario, detalhar_user, deletar_usuario

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('deletar/<int:id>/', deletar_usuario, name='deletar'),
    path('registrar/', register, name='register'),
    path('listar/usuarios/', listar_usuarios, name='listar_usuarios'),
    path('edit/user-funcionario/<int:id_user>/', edit_user_funcionario, name='edit_user_funcionario'),
    path('detalhar/user-funcionario/<int:id>/', detalhar_user, name='detalhar_user_funcionario'),
    # segurança
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')

]