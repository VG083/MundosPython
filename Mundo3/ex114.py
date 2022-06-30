# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mERRO, NÃO CONSEGUI ACESSAR O SITE\033[m')
else:
    print('O site está funcionando normalmente')
