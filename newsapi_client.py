import requests
from utils import is_valid_string
from newsapi_auth import NewsApiAuth

class NewsApiClient():
    def __init__(self, api_key, session):
        self.auth = NewsApiAuth(api_key=api_key)
        if session:
            self.request_method = session
        else:
            self.request_method = requests

    def get_by_headline(self, q=None):
        
        payload = {}

        if q is not None:
            if is_valid_string(q):
                payload['q'] = q
            else:
                raise TypeError("Invalid type of string")

 



        res = self.request_method.get("http://newsapi.org/v2/top-headlines", auth=self.auth, timeout=30, params=payload)
        
        if res.status_code != requests.codes.ok:
            print("Error: ")

        return res.json()

    

