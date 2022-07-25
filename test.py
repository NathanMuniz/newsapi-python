from distutils import core
import re
from tabnanny import check 

"""

# . - Entende qualquer valor exeto uma nova linha 
# \. - Para bucar o caracter "."


text = "arara"
text2 = "this. is a second text."
patter = re.compile(r"ar.ra")
patter2 = re.compile("\.")
check = patter.findall(text)
check2 = patter2.findall(text2)
print(check)
print(check2)



# ^ - Irá testar o início da string
# [^] - irá considerar todos os caracter EXETO o indicado
text = 'arara'
p1 = re.compile('^a')
p2 = re.compile('[^a]')
check1=p1.findall(text)
check2=p2.findall(text)
print(check1)
print(check2)


# \d Qualuqer caracter que SEJA um algorismo de 0 a 9 
text = "arara1992"
p1 = re.compile(r'\d')
p2 = re.compile(r'\D')
check1=p1.findall(text)
check2=p2.findall(text)
print(check1)
print(check2)


# \s - Qualquer cacaracter que SEJA vazio
# \S - Qualquer caracter que Não SEJA vazio
text = '''

arara 1992

'''
p1 = re.compile(r'\s')
p2 = re.compile(r'\S')
check1 = p1.findall(text)
check2 = p2.findall(text)
print(check1)
print(check2)

# \w Qualquer caracter que Seja alfanumérico
# \W - qualquer caracter que NÃO Seja alfanumérico
text = '''

_arara@ 1992_

'''

p1=re.compile(r'\w')
check1=p1.findall(text)
p2=re.compile(r'\W')
check2=p2.findall(text)
print(check1)
print(check2)

text = 'arara'
p1 = re.compile(r'r')
check_findall = p1.findall(text)
check_match = p1.match(text)
check_search = p1.search(text)
print(check_findall)
print(check_match)
print(check_search)



check_finditer = p1.finditer(text)

correspondencias = check_finditer
for corres in correspondencias:
    print(corres)

print(check_finditer)

"""

# Character set
text = '''
Arara 1993
'''

p = re.compile(r'[a-zA-Z] [0-9]')
correspondencias = p.finditer(text)
for coresp in correspondencias:
    print(coresp)

