from math import ceil

_300MbPS = 300
# TODO obter do banco de dados


def _obter_quantidade_de_roteadores(cobertura: int):
    return ceil(cobertura / 300)


def _calcular_roteadores(orcamento: dict):
    if _300MbPS >= orcamento['velocidade']:
        result = 699.90
        # TODO obter do banco de dados
    else:
        result = 779.90
        # TODO obter do banco de dados

    quantidade_de_roteadores = _obter_quantidade_de_roteadores(orcamento['cobertura'])
    return result * quantidade_de_roteadores


def _calcular_taxa_instalacao():
    return 99.9
    # TODO obter do banco de dados


def _calcular_desktops(orcamento: dict):
    if _300MbPS >= orcamento['velocidade']:
        result = 189.90
        # TODO obter do banco de dados
    else:
        result = 219.90
        # TODO obter do banco de dados
    return (result + _calcular_taxa_instalacao()) * orcamento['desktops']


def _calcular_notebooks(orcamento: dict):
    # TODO obter do banco de dados
    result = 259.90 + _calcular_taxa_instalacao()
    return result * orcamento['notebooks']


def calcular(orcamento: dict):
    roteadores = _calcular_roteadores(orcamento)
    desktops = _calcular_desktops(orcamento)
    notebooks = _calcular_notebooks(orcamento)
    return roteadores + desktops + notebooks
