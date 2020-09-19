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
        response = enviar(orcamento)
        response = salvar(orcamento)
    except Exception as e:
        print('Erro desconhecido, solicitanto orçamento.')
        print(e)
    return response


def calcular_valor_total(orcamento):
    orcamento['total'] = "%.2f" % calcular(orcamento)
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
