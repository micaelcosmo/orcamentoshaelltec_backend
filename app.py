from chalice import Chalice

from chalicelib.email import EmailSender

app = Chalice(app_name='orcamentoshaelltec')

@app.route('/orcamento', methods=['POST'])
def solicitar_orcamento():
#   # This is the JSON body the user sent in their POST request.
    orcamento = app.current_request.json_body
#   # Disparar email para Haelltec
    ## montar email
    ## enviar email montado
#   # Se disparou com sucesso, guarda no banco
#   # Se não, loga o erro
    return {}

def salvar_orcamento(orcamento):
    try:
        print(orcamento)
# guarda orcamento com status solicitada
    except Exception as e:
        print(e, "Erro ao salvar orçamento")


def montar_email():
# ler o template.html e carregar na variavel
# substituir as variaveis (replace)
# retornar string email com os valores substituidos
    return

def guarda_banco():
    return

def enviar_email(orcamento):
    return EmailSender.enviar_email(orcamento)