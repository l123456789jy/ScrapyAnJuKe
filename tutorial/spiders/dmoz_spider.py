# -*- coding: UTF-8 -*-
import scrapy
from scrapy.spider import Spider, Request
from scrapy.selector import Selector

from tutorial.items import AnJuKeItem


# 抓取安居客
class DmozSpider(Spider):
    name = "tutorial"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://bj.zu.anjuke.com/ditie/dt20-l2-s435/"
    ]

    def parse(self, response):
        sel = Selector(response)
        titleList = sel.xpath('//div/h3/a')
        for sel in titleList:
            item = AnJuKeItem()
            item['link'] = sel.xpath('@href').extract()
            yield scrapy.Request(item['link'][0], callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):
        sealsSea = Selector(response)
        nameList = sealsSea.xpath('//div/h2')
        phoneList = sealsSea.xpath('.//*[@id=\'content\']/div[2]/div[2]/div[2]/div[1]/div[3]')
        addressList = sealsSea.xpath('.//*[@id=\'content\']/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/dl[5]/dd/a')
        for sel in nameList:
            item = AnJuKeItem()
            item['name'] = sel.xpath('text()').extract()
            print item['name'][0]
            yield item

            for sel2 in phoneList:
                item = AnJuKeItem()
                item['phone'] = sel2.xpath('text()').extract()
                print item['phone'][0]
                yield item

            for sel3 in addressList:
                item = AnJuKeItem()
                item['address'] = sel3.xpath('text()').extract()
                print item['address'][0]
                yield item
