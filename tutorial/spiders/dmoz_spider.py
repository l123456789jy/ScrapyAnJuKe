from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import AnJuKeItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://bj.zu.anjuke.com/ditie/dt20-s435/"
    ]

    def parse(self, response):
        sel = Selector(response)
        titleList = sel.xpath('//div/h3/a')
        for sel in titleList:
            item = AnJuKeItem()
            item['link'] = sel.xpath('@href').extract()
            item['title'] = sel.xpath('text()').extract()
            yield item
