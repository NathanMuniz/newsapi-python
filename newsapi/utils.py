from __future__ import unicode_literals

import datetime
import re
import sys

# Definimos um nome para os modulos, quando importar esse módulo inteiro
# Esse nome é stringfy_date_param

__all__ = ("stringfy_date_param",)


#  [ valid_string ]
# Iremo criar duas const, PY2 e PY3, que pegam a versão do python
# ele usa o sys
# Irá criar uma função de is_valid_string, porém irá
# primeiro verificar se a a versão, e para cada versão irá ter uma
# valid string diferent. 
    # Se a for versão 3
        # a função valid string irá apenas verificar se a variávels
        # passada é um instancia de str
    # Se for a versão 2 
        # irá verificar se a variável passada é basestring
    # se não fo nenhum desse
        # irá lançar erro, que o python não suporta esse tipo.
        # Esse erro é um System erro 

# [ validate_dateime_str ]
# recebe parâmtro uma datastr
# Verfifica se a 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# #