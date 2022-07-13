from __future__ import unicode_literals
from django.forms import RadioSelect

import requests

from newsapi import const
from newsapi.newsapi_auth import NewsApiAuth
from newsapi.newsapi_exception import NewsAPIException
from newsapi.utils import is_valid_string, stringify_date_param


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

    #Inicalizador, coloque os parêmetros que serão usados
    # Defina varivél auth, que será um novo Objeto da nossa api, - preicsa passa a chav
    # Verifica se a session foi passada, se foi, então a definirmeos varia´vel request_method, com a sessio
    # se não o request_method será o request.
    # #

    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session


    

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
    # Função que iremos usar para definir o que buscar nas headlines. Ela 
    # basicamente recebe va´rios parêmtros em para cada parâmetro verificamos
    # se esse parâmetro foi passado.
    # #


    def get_top_headlines(  # noqa: C901
        self, q=None, qintitle=None, sources=None, language="en", country=None, category=None, page_size=None, page=None
    ):
        # Cria objeto Paylod, que será usado para tranferir as coisas importantes da API.

        payload = {}


        # Verifica se a variável q foi passada
            # Se foi -> irá irá verificar se o q é uma string válida, usando a validação do newspia
            # Se for então iremos usar um objeto "payload", que servira para carregar dados úteis da nossa api
                # e passaremos para ele nosso q.
            # Se não for valido -> ele irá chmar um erro de typo, e passar uma mensagem.
        if q is not None:
            if is_valid_string(q):
                payload['q'] = q
            else:
                raise TypeError("O valor q precisa ser uma str!")
    

        if (sources is not None) and ((country is not None) or (category is not None)):
            raise ValueError("cannot mix country/category param with sources param.")

        # Keyword/Phrase in Title. Mesma coisa do q.
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload['qintitle'] = qintitle
            else:
                raise TypeError("O valor qinline preicsa ser uma str")
    
        # Sources -> mesma coisa do q.
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
        else:
            raise TypeError("sources param should be of type str")

    
        # Lenguagem -> mesma coisa do q, porém tem um passo a mais
        # para verificar se a lenguagem está na const de lengauges

        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload["language"] = language
                else:
                    raise ValueError("invalid language")
            else:
                raise TypeError("language param should be of type str")
    
        
        # Controy , mesma coisa porém ele verifica que o contry passado está na lista de cost de
        # contries

        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else:
                raise TypeError("country param should be of type str")

        
        
        #Category - mesma coisa porém verifica se a categoria está nas constantes
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] = category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param should be of type str")




        # Page size, verifica se o tipo é int. Verficair se ele está entre o e 100. Tem um else 
        # para cada if

        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")

    
        
        # Page - mesma coisa do page_size, porém tem que ser apenas mairo que 0
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")

        
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
    

    
    # Função get_everyting
    # param: q, qintile, sources, domains, exlude_damins, from_param, to,
    # language, sort_by, page, page_size

    def get_everything(  # noqa: C901
        self,
        q=None,
        qintitle=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_param=None,
        to=None,
        language=None,
        sort_by=None,
        page=None,
        page_size=None,
    ):       
        # Cria um objeto paylod, e vai reficiado os algumentos passados
        # 
    
        payload = {}

        # q - Phrase [same as before]
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q
            else:
                raise TypeError("keyword/phrase q param should be of type str")
    
        # qintitle - Phrase [same as before]
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("keyword/phrase qintitle param should be of type str")

        # sources - [Same as Before]
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
            else:
                raise TypeError("The param sources need to be type str")
        
        # domais - Smae
        if domains is not None:
            if is_valid_string(domains):
                payload["domains"] = domains
            else:
                raise TypeError("domains param should be of type str")
            

    

        # exclude_domains 
        # faz verificação do se é none
        # verifica se o domínio, é uma instância de str, ou sejá, se ele é uma str
        # então adiciona no payload
        # e caham uma erro de tipo

        if exclude_domains is not None:
            if isinstance(exclude_domains, str):
                payload["excludeDomains"] = exclude_domains
            else:
                raise TypeError("exclude_domains param should be of type str")


        # verifica se o from_param is not not
        # adiciona o no payload, como from, porém ele irá usar a função strinfy_data_para
        # e passra nela nosso from_param

        if from_param is not None:
            payload["from"] = stringify_date_param(from_param)
        

        # To This Date
        # Verifica se não é none
        # adcionando no payload usnado stringy

        if to is not None:
            payload["to"] = stringify_date_param(to)

        # Language o mesmo de antes
        if language is not None:
            if is_valid_string(language):
                if language not in const.languages:
                    raise ValueError("invalid language")
                else:
                    payload["language"] = language
            else:
                raise TypeError("language param should be of type str")
        
        # Sort Method
        # Verifica que não é none
        # Verifcia é uma string válida
        # Verficia se está na const
        # Então adicioanr no payldo como sortBy 
        # e tem as exeptions

        if sort_by is not None:
            if is_valid_string(sort_by):
                if sort_by in const.sort_method:
                    payload["sortBy"] = sort_by
                else:
                    raise ValueError("invalid sort")
            else:
                raise TypeError("sort_by param should be of type str")

        # Page_zie
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")  

        # Page 
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")
        
        # Evia o request, usando a passando
        # url: const.EVERTHING_URL,
        # auth= self.auth
        # timeout = 30 
        # params = payload
        # joga na variável r

        r = self.request_method.get(const.EVERYTHING_URL, auth=self.auth, timeout=30, params=payload)



        # Checa se setá tudo ok com o status do request
        # Se não estiver, lança um NewsAPIException, passano json da nossa requisição
        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        # retona o json de nossa requisição.       
        return r.json()

    # função get_soruces
    # param: category, language, contry
    def get_sources(self, 
    category=None,
    language=None,
    country=None
    ):

    # paylodad
        payload = {}
    

    # verificação da linguagem padrão

        if language is not None:
            if is_valid_string(language):
                if language in const.language:
                    payload["langauge"] = language
                else:
                    raise ValueError("Invalid Lanaguage")
            else:
                raise TypeError("language param shoud be type str")

    # verificação do contry padrão

        if country is not None:
            if is_valid_string(country):
                if country in const.country:
                    payload["country"] = country
                else:
                    raise ValueError("Invalid Country")
            else:
                raise TypeError("coutry param should be type str")

    # verficação da category padrão

        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["categroy"] = category
                else:
                    raise ValueError("Invalid Category")
            else:
                raise TypeError("category param should be type str")

    # envia o resquest 
    # url: cosnt.SOURCES_URL
    # auth: self.auth
    # timeout: 30
    # params = paylaod

        r = self.request_method.get(const.SOURCES_URL, auth=self.auth, timeout=30, params=payload)

    # veriica se o request está ok
        if r.requests.code != requests.code.ok:
            raise NewsAPIException(r.json())
    
    # retorna o json.
  
        return r.json()

