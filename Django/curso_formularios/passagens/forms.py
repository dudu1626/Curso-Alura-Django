from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .classe_viagem import tipos_de_classe
from .validation import *
#########
from .models import Pessoa, Passagem, ClasseViagem

"""
# método de criação de formulário por meio do Forms
class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data Pesquisa', disabled=True,
                                    initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do Vôo', choices=tipos_de_classe)

    informacoes = forms.CharField(label='Informações extras', max_length=200,
                                  widget=forms.Textarea(), required=False)

    email = forms.EmailField(label='E-mail', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}

        campo_com_numero(origem, 'origem', lista_erros)
        campo_com_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_que_data_hoje(data_ida, data_pesquisa, lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data
"""


# Método de criação por meio do Models


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data Pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta',
                  'informacoes': 'Informações', 'classe_viagem': 'Classe do vôo'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}

        campo_com_numero(origem, 'origem', lista_erros)
        campo_com_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_que_data_hoje(data_ida, data_pesquisa, lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        # fields = ['email'] # diz quais os campos vão aparecer
        exclude = ['nome']  # diz quais os campos não vão aparecer

