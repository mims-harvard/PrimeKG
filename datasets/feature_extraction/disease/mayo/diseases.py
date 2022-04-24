# -*- coding: utf-8 -*-
import scrapy


class DiseasesSpider(scrapy.Spider):
    name = 'diseases'
    allowed_domains = ['www.mayoclinic.org']
    start_urls = ['https://www.mayoclinic.org']

    def parse(self, response):
        letters = response.xpath("//ol[@class='acces-alpha']/li/a")
        for letter in letters:
            link = letter.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_letter)

    def parse_letter(self, response):
        diseases = response.xpath("//div[@id='index']/ol/li/a")
        for disease in diseases:
            yield {
                "name": ' '.join(disease.xpath(".//text()").getall()),
                "link": 'https://www.mayoclinic.org' + disease.xpath(".//@href").get()
            }
