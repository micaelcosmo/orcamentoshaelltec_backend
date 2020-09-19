from Math import ceil

_300MbPS = 300
# TODO obter do banco de dados


def obter_quantidade_de_roteadores(cobertura):
    return ceil(cobertura / 300)


def calcular_roteadores(orcamento):
    result = 1

    if (_300MbPS >= orcamento['velocidade']):
        result = 699.90
        # TODO obter do banco de dados
    else:
        result = 779.90
        # TODO obter do banco de dados

    quantidade_de_roteadores = obter_quantidade_de_roteadores(orcamento.cobertura);
    return result * quantidade_de_roteadores


def calcular_taxa_instalacao():
    return 99.9
    # TODO obter do banco de dados


def calcular_desktops(orcamento):
    result = 1

    if (_300MbPS >= orcamento['velocidade']):
        result = 189.90
        # TODO obter do banco de dados
    else:
        result = 219.90
        # TODO obter do banco de dados
    return (result + calcular_taxa_instalacao()) * orcamento['desktops']    


def calcular_notebooks(orcamento):
    # TODO obter do banco de dados
    result = 259.90 + calcular_taxa_instalacao()
    return result * orcamento.notebooks


class Calculator:

    def calcular(self, orcamento):
        roteadores = calcular_roteadores(orcamento)
        desktops = calcular_desktops(orcamento)
        notebooks = calcular_notebooks(orcamento)
        return roteadores + desktops + notebooks)
