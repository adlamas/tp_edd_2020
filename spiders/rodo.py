import scrapy
from scrapy.crawler import CrawlerProcess
import pdb

class RodoSpider(scrapy.Spider):
    name = 'rodo'
    start_urls = [
        'https://rodo.com.ar/productos/imagen-sonido/minicomponente.html'
    ]
    allowed_domains = ['https://www.rodo.com.ar']

    respuesta = []

    def parse(self, response):
        for producto in response.css(".item"):
            titulo = producto.css(".product-name a::text").get()
            precio = producto.css(".price::text").get()
            link = producto.css(".item a[href]").attrib['href']
            self.respuesta.append([titulo,precio,link])
