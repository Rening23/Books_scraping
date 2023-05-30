import bs4
import requests

'''crear url sin numero de pagina'''
url_base= "http://books.toscrape.com/catalogue/page-{}.html"

titulo_rating_alto=[]
'''lista vacia para ir agregando los titulos de libros con 4 o 5 estrellas'''

for pagina in range(1,51):

    url_pagina=url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,"lxml")

    '''variable para hacer una seleccion'''
    libros = sopa.select(".product_pod")

    '''#loop que itere en los libros de la clase'''
    for libro in libros:

        '''chequer que tengan 4 o 5 estrellas'''
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            titulo_libro=libro.select("a")[1]["title"]

            '''Almacenar cada libro en la lista creada al inicio'''
            titulo_rating_alto.append(titulo_libro)

'''Imprimir libros de 4 o 5 estrellas'''
for t in titulo_rating_alto:
    print(t)

