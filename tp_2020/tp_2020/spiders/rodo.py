import scrapy
from scrapy.crawler import CrawlerProcess
import datetime

class RodoSpider(scrapy.Spider):

    name = 'rodo'
    def __init__(self,url):
        self.urlbusqueda = url
        self.start_urls = [
            'https://rodo.com.ar/catalogsearch/result/?q=' + self.urlbusqueda
        ]

    respuesta = []
    allowed_domains = ['https://www.rodo.com.ar']

    def parse(self, response):
        for producto in response.css(".item"):
            titulo = producto.css(".product-name a::text").get()
            precio = producto.css(".price::text").get()
            link = producto.css(".item a[href]").attrib['href']
            date_now = datetime.datetime.now()
            self.respuesta.append([titulo,precio,link,date_now.__str__()])
