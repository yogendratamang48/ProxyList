# -*- coding: utf-8 -*-
import scrapy
from proxyCollect.items import *


class FreeproxySpider(scrapy.Spider):
    name = "freeproxy"
    output_name='httpproxies.txt'
    allowed_domains = ["free-proxy-list.net"]
    start_urls = (
        'http://www.free-proxy-list.net/',
    )

    def parse(self, response):
        ipXpath = '//table[@id="proxylisttable"]/tbody/tr/td[1]/text()'
        portXpath = '//table[@id="proxylisttable"]/tbody/tr/td[2]/text()'

        ips = response.xpath(ipXpath)
        ports = response.xpath(portXpath)
        item = ProxycollectItem()

        for ip, port in zip(ips, ports):
            item['proxyAddress'] = 'http://'+str(ip.extract())+":"+str(port.extract())
            yield item
        
class SslproxySpider(scrapy.Spider):
    name = "sslproxy"
    output_name='sslproxies.txt'
    allowed_domains = ["sslproxies.org"]
    start_urls = (
        'https://www.sslproxies.org/',
    )

    def parse(self, response):
        ipXpath = '//table[@id="proxylisttable"]/tbody/tr/td[1]/text()'
        portXpath = '//table[@id="proxylisttable"]/tbody/tr/td[2]/text()'

        ips = response.xpath(ipXpath)
        ports = response.xpath(portXpath)
        item = ProxycollectItem()

        for ip, port in zip(ips, ports):
            item['proxyAddress'] = 'https://'+str(ip.extract())+":"+str(port.extract())
            yield item
        
