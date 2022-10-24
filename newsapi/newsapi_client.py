from newsapi_auth import NewsApiAuth
import requests


class NewsApiClient():
    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is not None:
            self.request_method = requests
        else:
            self.request_method = session

    def get_top_headline( 
            q=None, qintitle=None, language='en', ):

        payload = {} 

        if q is not None:
            if q 
