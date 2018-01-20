import scrapy
import json
from ganji.items import GanjiItem


class GanjiSpider(scrapy.Spider):
    name = "ganji"
    allowed_domains = ["sh.ganji.com"]
    start_urls = ["http://sh.ganji.com/zufang/agent/"]

    def parse(self, response):
        for sel in response.css('.f-list-item'):
            item = GanjiItem()
            item['name'] = sel.css('.broker-name ::text').extract()
            item['phone'] = sel.css('.tel ::text').extract()
            yield item

        next_page = response.css('.next ::attr(href)').extract()
        print('------------------------------------------------------------------')
        print(next_page)
        if next_page:
            print('------------------------------------------------------------------')
            next_href = next_page[0]
            next_page_url = 'http://sh.ganji.com' + next_href
            print(next_page_url)
            request = scrapy.Request(url=next_page_url)
            yield request
