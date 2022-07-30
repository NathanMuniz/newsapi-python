
from newsapi_auth import NewsApiAuth
from utils import is_valid_string, stringify_date_param 

import requests

import const
from newsapi_exception import NewsApiExeception



class NewsApiClient(object):

    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is not None: 
            self.conxtext_request = session
        else:
            self.conxtext_request = requests

    def get_top_headline(self, q=None, qintitle=None, source=None, language=None, country=None):
        
        payload = {}

        if q is not None:
            if is_valid_string(q):
                payload['q'] = q
            else:
                TypeError('q must be a valid string')

        if qintitle is not None:
            if is_valid_string(qintitle):
                payload['qintitle'] = q
            else:
                TypeError('qintitle must be a valid string')

        
        if source is not None and ((country is not None) or language is not None):
            raise ValueError("The source cannot be passed mixed with coutry or language")

        if source is not None:
            if is_valid_string(source):
                payload['source'] = source
            else:
                TypeError('q must be a valid string')
        
        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload['language'] = language
                else:
                    ValueError("Language must to be in the sigla format")
            else:
                TypeError("Lanauge must to be a valid string")

        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload['country'] = country
                else:
                    ValueError("Country must to be in the sigla format")
            else:
                TypeError("Coutry must to be a valid string")
        
        r = self.conxtext_request.get(const.TOP_HEADLINES_URL, self.auth, timeout=30, params=payload)

        if r.request_code != requests.request_code_ok:
            raise NewsApiExeception(r.json())

        return r.json()






