from requests.auth import AuthBase

class NewsApiAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key 

    def __call__(self, requests):
        requests.headers.update(get_auth_headers(self.api_key))
        return requests
    
def get_auth_headers(api_key):
    return {"Content-Type": "Application/JSON", "Authorizatino": api_key}

