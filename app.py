from chalice import Chalice

from chalicelib.calculator import calcular
from chalicelib.email import EmailSender

app = Chalice(app_name='orcamentoshaelltec')


@app.route('/orcamento', methods=['POST'])
def solicitar_orcamento():
    orcamento = app.current_request.json_body
    response = {}
    try:
        calcular_valor_total(orcamento)
        orcamento = obter_consultor_disponivel(orcamento)
        response = enviar(orcamento)
        response = salvar(orcamento)
    except Exception as e:
        print('Erro desconhecido, solicitanto orçamento.')
        print(e)
    return response


def obter_consultor_disponivel(orcamento):
    orcamento['consultor'] = 'Micael M A Cosmo'
    return orcamento
#   TODO obter consultor que tiver disponível


def calcular_valor_total(orcamento):
    total = calcular(orcamento)
    return formatar_valor(orcamento, total)


def formatar_valor(orcamento, total):
    orcamento['total'] = "R${:.2f}".format(total)
    return orcamento


def salvar(orcamento):
    try:
        return {
            "ResponseMetadata": dict(HTTPStatusCode=200, orcamento=orcamento)
        }

    # TODO guarda orcamento com status solicitada
    except Exception as e:
        print(e, "Erro ao salvar orçamento")
        return {
            "ResponseMetadata": dict(HTTPStatusCode=500)
        }


def guarda_banco():
    pass


def enviar(orcamento):
    return EmailSender().enviar_email(orcamento)
