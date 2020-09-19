from chalice import Chalice

from chalicelib.email import EmailSender

app = Chalice(app_name='orcamentoshaelltec')


@app.route('/orcamento', methods=['POST'])
def solicitar_orcamento():
    #   # This is the JSON body the user sent in their POST request.
    print(app.current_request.json_body)
    orcamento = app.current_request.json_body
    try:
        response = enviar(orcamento)
        salvar(orcamento)
    except Exception as e:
        print('Erro desconhecido, solicitanto orçamento.')
        print(e)
    return {}


def salvar(orcamento):
    try:
        print(orcamento)
    # guarda orcamento com status solicitada
    except Exception as e:
        print(e, "Erro ao salvar orçamento")


def guarda_banco():
    return


def enviar(orcamento):
    return EmailSender().enviar_email(orcamento)
