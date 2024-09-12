import requests
import pandas as pd
from bs4 import BeautifulSoup

resp = requests.get('https://jovempan.com.br/noticias/economia')
# print(resp.content)

site = BeautifulSoup(resp.text, 'html.parser')
# print(site.prettify())

noticias = site.find_all('div', {'class': 'highlight-item'})
noticias += site.find_all('article', {'class': 'type-post'})
# print(noticia.prettify())

lista_noticias = []

for noticia in noticias:
    titulo = noticia.find('h2')

    tag_a = titulo.find('a')

    # print(titulo.prettify())

    titulo = titulo.text

    if 'Argentina' in titulo:
        lista_noticias.append([titulo, tag_a])
        print(tag_a['href'])

df = pd.DataFrame(lista_noticias, columns=['Titulo', 'Link'])
# index=False, não vai aparecer o index das linhas!
df.to_csv('noticias.csv', index=False)