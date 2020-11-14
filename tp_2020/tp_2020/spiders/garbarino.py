import scrapy
from scrapy.crawler import CrawlerProcess
import datetime

class GarbarinoSpider(scrapy.Spider):

    name = 'garbarino'
    def __init__(self,url):
        self.urlbusqueda = url
        self.start_urls = [
            'https://www.garbarino.com/q/' + self.urlbusqueda + '/srch?q=' + self.urlbusqueda
        ]
        print(self.start_urls)

    respuesta = []
    #allowed_domains = ['https://www.garbarino.com/']

    def parse(self , response):
        for producto in response.css(".col-md-3"):
            titulo = producto.css(".itemBox--title::text").get()
            precio = producto.css(".value-item::text").get()
            link = producto.css(".block").attrib["href"]
            date_now = datetime.datetime.now()
            self.respuesta.append([titulo,precio,"https://www.garbarino.com"+ link,date_now.__str__()])
