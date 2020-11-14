import scrapy
from scrapy.crawler import CrawlerProcess
import datetime

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
            titulo = producto.css(".akEoc::text")[1].get()
            precio = producto.css(".egaLpU::text").get()
            link = "https://www.fravega.com" + producto.css(".hlRWOw a[href]").attrib['href']
            date_now = datetime.datetime.now()
            self.respuesta.append([titulo,precio,link,date_now.__str__()])
