# Classe NewsAPIException - extendo from exception 

from logging import exception


class NewsAPIException(exception):
    def __init__(self, exception):
        self.exception = exception
    
    def get_exception(self):
        if self.exception["status"]:
            return self.exception["status"]
    
    def get_code(self):
        if self.exception["code"]:
            return self.exception["code"]
    
    def get_message(self):
        if self.exception["message"]:
            return self.exception["message"]


# inicializador
# param: exceptinon - pega parametro 

# método get_exception
# verifica se o exception, na key status foi passsado
# se foi, etnão ele retornará a execption na key status

# método get_code
# verifica se o expetion, na key code, foi passado
# se foi ele irá o retonar

# método get_message
# verifica se o exception message foi passado
# se foi irá retornar ele