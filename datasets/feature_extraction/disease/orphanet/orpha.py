import scrapy
import logging
from urllib.parse import urljoin

class QuotesSpider(scrapy.Spider):
    name = 'disease_web_scrape'
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'RETRY_TIMES': '100'
    }
    start_urls = [
        'https://www.orpha.net/consor/cgi-bin/Disease_Search.php?lng=EN&search=Disease_Search_List'
    ]

    def parse(self, response):
        base_url = 'https://www.orpha.net/consor/cgi-bin/'
        #list = response.xpath('(//h3[text() = "Alphabetical list"]/following-sibling::div[1]//li/a)[1]/@href').get()
        #list_href = list[0].xpath('./@href').get()
        #request = scrapy.Request(urljoin(base_url, list), callback=self.parse_list)
        #yield request

        for alphabet in response.xpath('//h3[text() = "Alphabetical list"]/following-sibling::div[1]//li/a'):
            list_href = alphabet.xpath('./@href').get()
            request = scrapy.Request(urljoin(base_url, list_href), callback=self.parse_list)
            yield request

    def parse_list(self, response):
        logging.info(("List: " + response.request.url))
        base_url = 'https://www.orpha.net/consor/cgi-bin/'
        for disease in response.xpath('//div[@id = "result-box"]/ul/li/a'):
            disease_name = disease.xpath('./text()').get()
            disease_url = disease.xpath('./@href').get()
            request = scrapy.Request(urljoin(base_url, disease_url), callback=self.parse_content, errback=self.errback)
            request.meta['disease'] = disease_name
            yield request

    def parse_content(self, response):
        disease_shortname = response.meta['disease']
        disease_name = response.xpath("//h2[3]/text()").get()
        disease_id = response.xpath("//div[@class = 'idcard artBlock']/h3/text()").get()
        definition = response.xpath('//div[@class = "definition"]/section/p/text()').get()
        prevalence = response.xpath("//ul[@class = 'idData']//em[text()='Prevalence: ']/following-sibling::strong/text()").get()
        UMLS = response.xpath("//ul[@class = 'idData']//em[text()='UMLS: ']/following-sibling::strong/text()").get()
        epidemiology = response.xpath("//div[@class = 'articleInfo']/h3[contains(text(), 'Epidemiology')]/following-sibling::section[1]/p/text()").get()
        clinical_description = response.xpath("//div[@class = 'articleInfo']/h3[contains(text(), 'Clinical description')]/following-sibling::section[1]/p/text()").get()
        management_and_treatment = response.xpath("//div[@class = 'articleInfo']/h3[contains(text(), 'Management and treatment')]/following-sibling::section[1]/p/text()").get()
        yield{
            'disease_shortname': disease_shortname,
            'disease_name': disease_name,
            'disease_id': disease_id,
            'definition': definition,
            'prevalence': prevalence,
            'UMLS': UMLS,
            'epidemiology': epidemiology,
            'clinical_description': clinical_description,
            'management_and_treatment': management_and_treatment
        }

    def errback(self, response):
        logging.info(("ERROR: " + response.meta['disease']))
        request = scrapy.Request(response.request.url, callback=self.parse_content, errback=self.errback)
        yield request
