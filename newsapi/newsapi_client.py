from __future__ import unicode_literals

import requests

from newsapi import const 
from newsapi.newsapi_auth import NewsApiAuth
from newsapi.newsapi_exception import NewsApiException 
from newsapi.utils import is_valid_string, stringify_date_param 


class NewsApiClient(object):
    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is None:
            self.requests_method = requests
        else:
            self.requests_method = session

    def get_top_headlines( # noqa: C901
        self, q=None, qintitle=None, soruces=None, language="en", coutry=None, category=None, page_size=None, page=None
        ):
        payload = {}
        
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q 
            else:
                raise TypeError("Keyword/p")

        
