import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess

class CompumundoSpider(scrapy.Spider):
    name = 'compumundo'
    allowed_domains = ['www.compumundo.com.ar']
    respuesta = []

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    def __init__(self, busqueda=None, *args, **kwargs):
        super(CompumundoSpider,self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.compumundo.com.ar/q/{busqueda}/srch']

    def parse(self, response):
        sel = Selector(response)
        productos = sel.xpath('//div[@class="col-xs-12 col-sm-4 col-md-3"]')
        for producto in productos:
            titulo= producto.xpath('.//h3[@itemprop="name"]/text()').extract_first()
            precio= producto.xpath('.//span[starts-with(@id,"price")]/text()').extract_first()
            link= "https://www.compumundo.com.ar"+producto.xpath('.//a[@itemprop="url"]/@href').extract_first()
            self.respuesta.append([titulo,precio,link])
