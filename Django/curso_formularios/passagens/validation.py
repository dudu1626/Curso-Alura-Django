
def origem_destino_iguais(origem, destino, lista_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_erros['destino'] = "Origem e destino não podem ser iguais"


def campo_com_numero(valor_do_campo, nome_do_campo, lista_erros):
    """Verifica se tem caracter numérico no campos"""
    if any(char.isdigit() for char in valor_do_campo):
        lista_erros[nome_do_campo] = 'Campo não pode ter números'


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros):
    """Verificação das datas lançadas para que a ida não seja maior que a data de volta"""
    if data_ida > data_volta:
        lista_erros['data_volta'] = "Data de ida não pode ser maior que a data de volta!"


def data_ida_menor_que_data_hoje(data_ida, data_pesquisa, lista_erros):
    """Verificação da data de ida não seja menor que a data da pesquisa"""
    if data_ida > data_pesquisa:
        lista_erros['data_volta'] = "Data de ida não pode ser menor que a data de hoje!"

