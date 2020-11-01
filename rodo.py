import scrapy
from scrapy.crawler import CrawlerProcess
import pdb
import csv

class RodoSpider(scrapy.Spider):
    name = 'rodo'
    start_urls = [
        'https://rodo.com.ar/productos/imagen-sonido/minicomponente.html'
    ]

    def parse(self, response):
        peliculas = response.css('.product-name a::text').getall()
        pdb.set_trace()
        with open('productos_rodo.csv', mode='w') as archivo:
            archivo_csv = csv.writer(archivo, delimiter=',')
            for pelicula in peliculas:
                print(pelicula)
                archivo_csv.writerow([pelicula])

# run spider
