class NewApiExepetion(Exception):
    def __init__(self, exception):
        self.exception = exception
    
    def get_status(self):
        if self.exception['status']:
            return self.exception['status']
            
    def get_code(self):
        if self.exception['code']:
            return self.exception['code']

    def get_message(self):
        if self.exception['message']:
            return self.exception['message']
