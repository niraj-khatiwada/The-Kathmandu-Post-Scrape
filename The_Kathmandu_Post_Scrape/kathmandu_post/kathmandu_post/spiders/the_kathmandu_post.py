# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from fake_useragent import UserAgent

class TheKathmanduPostSpider(scrapy.Spider):
    name = 'the_kathmandu_post'
    ua = UserAgent()

    def start_requests(self):
        yield SeleniumRequest(
            url = "https://kathmandupost.com",
            wait_time= 3,
            screenshot= True,
            callback = self.parse,
            headers = {'User-Agent': TheKathmanduPostSpider.ua.random}

        )
    def parse(self, response):
       
        for article in response.xpath("//article[@class='article-image ']"):
            yield{
                'Title': article.xpath(".//a/h3/text()").get(),
                'Date':  response.xpath("//div[@class='blocktop blocktop-date hidden-xs hidden-sm']/text()").get().strip(),
                'Link': response.urljoin(article.xpath(".//a/@href").get()),
                'Description': article.xpath(".//p/text()").get(),
                'Thumbnail': article.xpath(".//div/figure/a/img/@data-src").get()
            }
