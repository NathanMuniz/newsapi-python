from webbrowser import get
from requests.auth import AuthBase 

class NewsApiAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key
    
    def __call__(self, request):
        request.headers.update(self.get_auth_headers(self.api_key))
        return request
    
    def get_auth_headers(api_key):
        return {'Content-type' : 'application/JSON', 'Authorization': api_key}