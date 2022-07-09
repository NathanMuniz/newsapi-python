import requests
from newsapi import const
from newsapi.newsapi_auth import NewsApiAuth 
from newsapi.newsapi_exception import NewsAPIException 
from newsapi.utils import is_valid_string, stringfy_date_param 


class NewsApiClient(object):
    """The core client object used to fetch data from News API endpoints.


    :param api_key: Your API key, a length-32 UUID string provided for your News API account. 
        you must `register <https://newsapi.org/register>`_ for a News API key. 
    :type api_key: str

    :param session: An optional :class:`requests.Session` instace from which to execute requests. 
    **Note**: If you provide a ``session``intance, :class:`NewsApiClient` will *not* close the session
    for you. Remembet to call ``session.close()``, or use session as a context manager, to close
    the socket and free up resources. 
    :type session: `request.session <https://2.python-request-org/en/master/user/advanced/#session-objects` _ or None    
    
    
    """

    def __init__(self, api_key, session=None):
        # Cria um nova comunicaçaõ com a api, para isso usa a objeto NewsApiAuth 
        #e nele ele passa a nossa key. 
        #Então joga essa conexão para, para uma variável padrão de nossa classe "auth".
        #
        self.auth = NewsApiAuth(api_key=api_key)

        # Verifica que a nossa session foi passada.
        #  SE  SIM-> irá definir a variável da classe request_method como sendo request que 
        #   importamos. Assim um variável que podemos fazer requests. 
        #    SE NÃO, então iremos definitor nossa request_method, sendo a nossa session    
        #
        if session is None:
            self.request_method = requests
        else: 
            self.request_method = session
        


    def get_top_headlines( # noqa: C901
    self, q=None, qintile=None, sources=None, langauge="en", country=None, category=None, page_size=None, page=None

    ):

        """ Call the `top-headlines` endpoint
        fetch live top and breaking headlines. 

        This endpoint provides live top and breakin headlines for a country, specific category in a country,
        single source, or multiple srouces. You can also search with keywords. Ariticle are sroted by 
        the earliest date published first.

        :param q: Keywords or a phase to search for in the article title and body. 
    
        
        """

        # Verifica se a variável q foi passada
            # Se foi -> irá irá verificar se o q é uma string válida, usando a validação do newspia
             # Se for então iremos usar um objeto "payload", que servira para carregar dados úteis da nossa api
                # e passaremos para ele nosso q.
            # Se não for valido -> ele irá chmar um erro de typo, e passar uma mensagem.
            
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q 
            else: 
                raise TypeError("Keyword/phrase q param shoud be of type str")
            

        #