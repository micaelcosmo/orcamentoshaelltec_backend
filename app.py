from chalice import Chalice

app = Chalice(app_name='orcamentoshaelltec')

@app.route('/orcamento', methods=['POST'])
def solicitar_orcamento():
#   # This is the JSON body the user sent in their POST request.
    orcamento = app.current_request.json_body
#   # Disparar email para Haelltec
#   # Se disparou com sucesso, guarda no banco
#   # Se não, loga o erro
    return {}
