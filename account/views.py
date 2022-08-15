from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import UserRegistrationForm, UserEditForm
from funcionarios.forms import FuncionarioForm
from funcionarios.models import Funcionario


@login_required(login_url='login')
def listar_usuarios(request):

    usuarios = User.objects.all().order_by('first_name').select_related('funcionario')

    paginator = Paginator(usuarios, 10)
    page_number = request.GET.get('pege')
    page_obj = paginator.get_page(page_number)

    return render(request, 'account/list-user.html', {'page_obj': page_obj})


@login_required(login_url='login')
def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user_form.save_m2m()

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')

    else:

        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})


@login_required(login_url='login')
def edit_user_funcionario(request, id_user):

    user = get_object_or_404(User, pk=id_user)
    funcionario_id = user.funcionario.id
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        funcionario_form = FuncionarioForm(instance=funcionario, data=request.POST, files=request.FILES)

        if user_form.is_valid() and funcionario_form.is_valid():
            user_form.save()
            funcionario_form.save()
            messages.success(request, 'Dados atualizados com sucesso!!')
            return redirect('listar_usuarios')
    else:
        user_form = UserEditForm(instance=user)
        funcionario_form = FuncionarioForm(instance=funcionario)

    context = {
        'user_form': user_form,
        'funcionario_form': funcionario_form,
        'funcionario_db': funcionario
    }

    return render(request, 'account/edit.html', context)


@login_required(login_url='login')
def detalhar_user(request, id):
    user = get_object_or_404(User, pk=id)

    context = {
        'user': user,

    }

    return render(request, 'account/detalhe.html', context)


@login_required(login_url='login')
def deletar_usuario(request, id):

    usuario = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        if usuario:
            usuario.delete()
            messages.success(request, 'Usuário removido com sucesso!!')
            return redirect('listar_usuarios')
        else:
            messages.error(request, 'Não foi possível remover o usuário solicitado')
            return render(request, 'account/deletar.html')

    context = {
        'usuario': usuario
    }

    return render(request, 'account/deletar.html', context)
