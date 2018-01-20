import scrapy
import json
import re
from anjuke.items import AnjukeItem


class AnjukeSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["shanghai.anjuke.com"]
    start_urls = ["https://shanghai.anjuke.com/tycoon/"]

    def parse(self, response):
        print('------------------------------------------------------')
        for sel in response.css('.jjr-itemmod'):
            item = AnjukeItem()
            item['name'] = sel.css('.jjr-title h3 a::attr(title)').extract()
            phone = re.search('(\d{11})', str(sel.css('.jjr-side ::text').extract()),re.DOTALL)
            item['phone'] = phone.group(1)
            yield item

        next_page = response.css('.aNxt ::attr(href)').extract()
        print('------------------------------------------------------------------')
        print(next_page)
        if next_page:
            print('------------------------------------------------------------------')
            next_href = next_page[0]
            request = scrapy.Request(url=next_href)
            yield request
