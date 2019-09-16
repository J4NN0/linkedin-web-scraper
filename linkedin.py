# -*- coding: utf-8 -*-
import scrapy
from cookieManager import CookieManager


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'

    allowed_domains = ['linkedin.com']
    # start_urls = ['https://www.linkedin.com/']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookie)

    def parse(self, response):
        self.response = response

        name = self.response.xpath('//*[@id="ember58"]/h1/span').extract_first()
        overview = self.response.css('p.break-words white-space-pre-wrap mb5 t-14 t-black--light t-normal::text').get()
        website = self.response.css('span.link-without-visited-state::text').get()
        industry = self.response.css('dd.org-page-details__definition-text t-14 t-black--light t-normal::text').get()
        size = self.response.css('dd.org-about-company-module__company-size-definition-text t-14 t-black--light mb1 fl::text').get()
        typec = self.response.css('dd.org-page-details__definition-text t-14 t-black--light t-normal::text').get()
        founded = self.response.css('dd.org-page-details__definition-text t-14 t-black--light t-normal::text').get()
        specialities = self.response.css('dd.org-page-details__definition-text t-14 t-black--light t-normal').get()

        dic = dict()
        dic['name'] = name
        dic['overview'] = overview
        dic['website'] = website
        dic['industry'] = industry
        dic['size'] = size
        dic['type'] = typec
        dic['founded'] = founded
        dic['specialities'] = specialities

        yield {'Company': dic}

    def __init__(self, urls):
        super().__init__(urls)
        self.urls = urls
        self.response = None
        self.cookie = CookieManager().get_cookies()
