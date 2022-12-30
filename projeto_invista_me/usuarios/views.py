from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def novo_usuario(request):
    # Verificar tipo da requisição
    # Validar a informação
    # Informa se o usuário foi criado ou não
    # Salvar informação no banco de dados

    # 1
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST);
        if formulario.is_valid():
            # Salva no banco de dados
            formulario.save();
            # Informa o usuário
            usuario = formulario.cleaned_data.get('username');
            messages.success(request, f'o usuário {usuario} foi criado com sucesso!');
            return redirect('login');
    else:
        formulario = UserCreationForm()



    return render(request, 'usuarios/registrar.html', {'formulario': formulario});