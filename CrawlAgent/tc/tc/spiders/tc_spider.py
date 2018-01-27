import json
import scrapy
from tc.items import TcItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class Tc(scrapy.Spider):
    name = "tc"
    start_urls = ["http://sh.58.com/ershoufang/"]
    status = 200

    def parse(self, response):
        iten_number = 1
        for sel in response.css('.title'):
            iten_href = sel.css('.title ::attr(href)').extract()[0]
            print('parse----------------------------------------------------------------------------')
            agent_name = sel.xpath('/html/body/div[4]/div[5]/div[1]/ul/li[' + str(iten_number) + ']/div[2]/div/a/span/text()').extract()
            iten_number += 1
            child_page_request = scrapy.Request(url=iten_href,callback=self.parse_page2,meta={'name':agent_name })
            yield child_page_request

        next_page = response.css('.next ::attr(href)').extract()
        print('next_page------------------------------------------------------------------')
        if next_page:
            print('has_next_page------------------------------------------------------------------')
            next_href = next_page[0]
            print(next_href)
            next_page_request = scrapy.Request(url=next_href)
            yield next_page_request

    def parse_page2(self, response):
        print('parse_page2----------------------------------------------------------------------------')
        item = TcItem()
        item['name'] = response.meta['name']
        item['phone'] = response.css('.phone-num ::text').extract()
        yield item
