import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O Youtube não está acessível no momento.')
else:
    print('Consegui acessar o Youtube com sucesso.')