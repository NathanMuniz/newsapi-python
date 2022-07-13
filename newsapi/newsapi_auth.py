from requests.auth import AuthBase 

# Classe NewsApiAuth - herda do AuthBase 

class NewsApiAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key
    
    def __call__(self, request):
        request.headers.update(get_auth_headers(self.api_key))

    def get_auth_headers(api_key):
        return {"Content-type" : "application/JSON", "Authorization" : api_key}



# inicializador
# param: api_key -> pega ele

# Usa o método interno call para usar como instância do iniciazliador
# param: request 
# pega o headers do nosso request, e adiciona no retorno do nosso get_auth_header.
# e passa a api, da nossa aplicação, para ela.

# Função get_auth_headers
# Param: api_key
# retonar: Dicionário que tem, key 'Content-type" value "application/JSON", "Authoriztion" : api_key