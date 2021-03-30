from django.shortcuts import render, get_object_or_404, redirect
from apps.receitas import Receita
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_a_exibir)


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        if campo_vazio(nome_receita):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        ingredientes = request.POST['ingredientes']
        if campo_vazio(ingredientes):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        modo_preparo = request.POST['modo_preparo']
        if campo_vazio(modo_preparo):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        tempo_preparo = request.POST['tempo_preparo']
        if campo_vazio(tempo_preparo):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        rendimento = request.POST['rendimento']
        if campo_vazio(rendimento):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        categoria = request.POST['categoria']
        if campo_vazio(categoria):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cria_receita')

        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        # maneira de pegar o usuário na requisição
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita,
                                         ingredientes=ingredientes, modo_preparo=modo_preparo,
                                         tempo_preparo=tempo_preparo, rendimento=rendimento,
                                         categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
    return redirect('dashboard')


def campo_vazio(campo):
    """Função para tratar o campo apenas com espaço"""
    return not campo.strip()
