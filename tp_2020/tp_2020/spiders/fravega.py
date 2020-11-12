import scrapy
from scrapy.crawler import CrawlerProcess

class FravegaSpider(scrapy.Spider):

    name = 'fravega'
    def __init__(self,url):
        self.urlBusqueda = url
        self.start_urls = [
            'https://www.fravega.com/l/?keyword=' + self.urlBusqueda
        ]

    respuesta = []
    allowed_domains = ['https://www.fravega.com']

    def parse(self, response):
        for producto in response.css(".hlRWOw"):
            titulo = producto.css(".akEoc::text").get()
            precio = producto.css(".egaLpU::text").get()
            link = producto.css(".hlRWOw a[href]").attrib['href']
            self.respuesta.append([titulo,precio,link])
