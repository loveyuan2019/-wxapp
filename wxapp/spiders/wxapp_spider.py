# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title=response.xpath(r"//h1[@class='ph']/text()").get()
        author=response.xpath(r"//p[@class='authors']/a/text()").get()
        pub_time=response.xpath(r"//span[@class='time']/text()").get()
        content=response.xpath(r"//div[@class='blockquote']/p/text()").get()
        
        item=WxappItem(title=title,author=author,pub_time=pub_time,content=content)
        yield item



        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
