from bs4 import BeautifulSoup
import requests

r     = requests.get('https://www.meuip.com.br/')
fonte = r.content

if ( r.ok == False):
 print('Fracasso')

#r.content será a fonte do código a ser analizado
soup = BeautifulSoup(fonte,"html.parser")
ip=soup.h3.text.replace("Meu ip é","").replace(" ","")
print("IP :{0}".format(ip))