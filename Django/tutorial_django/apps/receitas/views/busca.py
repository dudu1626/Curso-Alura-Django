from apps.receitas import Receita
from django.shortcuts import render


def busca(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'search' in request.GET:  # o nome está assim por causa do botão do html,
                                 # poderia estar em português
        nome_a_buscar = request.GET['search']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas,
    }

    return render(request, 'receitas/buscar.html', dados)
