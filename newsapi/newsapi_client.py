from pytz import country_timezones
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
    self, q=None, qintitle=None, sources=None, langauge="en", country=None, category=None, page_size=None, page=None

    ):

        """ Call the `top-headlines` endpoint
        fetch live top and breaking headlines. 

        This endpoint provides live top and breakin headlines for a country, specific category in a country,
        single source, or multiple srouces. You can also search with keywords. Ariticle are sroted by 
        the earliest date published first.

        :param q: Keywords or a phase to search for in the article title and body. 
        :type q: str or None

        :param qintitle: Keywords to a phrase to search for in the article title and body.
        :type sintle: str

        :param sources: A comma-separates string of indentifier for the news sources or blog you 
        wnat headline from.
        :param:

        :param language: The 2-letter ISO-639-1 code fo the languge you wuant ot get headlines for.
        :type languge: str or None

        :param country: The 2-letter ISO 3166-1 code fo the contry you qnat ot get headlines for.
        :type country: str or None

        :param category: The category you want to get headlines for.
        :type category: str or None

        :param_size: Use this to page throught the results fi the total resutla found is greater thean
        the page size.
        :type page_size: int or None

        :param page: The number of results to return per page (request).
            20 is the default, 100 is the maximum.
        :type page: int or None

        return: JSON resposne as nasted Python dictionary.
        :rtype: dict
        :raises NewsAPIException: If the ``"status"`` value of the resposne is ``"error"`` rather than ``"ok"``. 


        """


        # Cria objeto Paylod, que será usado para tranferir as coisas importantes da API.

        payload = {} 

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
            

        # Keyword/Phrase in Title. Mesma coisa do q.
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("Keyword/phrase qintitle param sould be of type str")
        

        # Sources -> mesma coisa do q.
        if sources is not None:
            payload["sources"] = sources 
        else: 
            raise TypeError("srouces param shoud be type of str")

        # Lenguagem -> mesma coisa do q.
        if langauge is not None:
            if is_valid_string(sources):
                payload["sources"] = sources 
            else: 
                raise TypeError("srouces param soud be of type str")
        
        # Controy , mesma coisa porém ele verifica que o contry passado está na lista de cost de
        # contries
        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else: 
                raise TypeError("country param shoud be of type str")
        
        #Category - mesma coisa porém verifica se a categoria está nas constantes
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] - category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param shoud be of type str")




        # Page size, verifica se o tipo é int. Verficair se ele está entre o e 100. Tem um else 
        # para cada if
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size 
                else:
                    raise ValueError("page_size param should b an int between 1 and 100")
            else:
                raise ValueError("page_size param shoud be an int")
        
        # Page - mesma coisa do page_size, porém tem que ser apenas mairo que 0
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page 
                else:
                    raise ValueError("Page param shoud be an int greater than 0")
            else:
                raise TypeError("page param shoud be an int")
        
        # Send Request - usa o request_method para fazer um get. Ele irá passar os seguinte parametos
        # url: Pagara da nossa cont, url de headline
        # auth: que será nosso auth
        # timeout: será 30
        # params: será payload
        # Ele joga toda essa requisição get, dentro da variável r
        r = self.request_method.get(const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request  - Verifica se nossa requisão tive um códido ruim, ou sejá
        # usando o requests.codes.ok, como comparação
        # Se naõ teve um retorno ok, então ele irá lançar um object NewAPIExeption, e passara um 
        # json, da nossa requisição
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())
        
        # então ele retorna o json da nossa requisição
        return r.json()
