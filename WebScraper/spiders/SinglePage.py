import scrapy
import tldextract


class SinglePageSpider(scrapy.Spider):

    name = 'SinglePage'

    def __init__(self, name=None, **kwargs):
        super(SinglePageSpider, self).__init__(name=name, **kwargs)
        self.data = {}
        ex = tldextract.extract(self.url)
        self.allowed_domains = [ex.registered_domain]
        self.start_urls = [self.url]

    def parse(self, response):
        self.data["uuid"] = self.uuid
        self.data["url"] = self.url
        self.data["email"] = self.email
        self.data["title"] = response.xpath('//title/text()').getall()
        self.data["link"] = response.xpath('//a/text()').getall()
        self.data["span"] = response.xpath('//span/text()').getall()
        self.data["paragraph"] = response.xpath('//p/text()').getall()
        self.data["heading 1"] = response.xpath('//h1/text()').getall()
        self.data["heading 2"] = response.xpath('//h2/text()').getall()
        self.data["heading 3"] = response.xpath('//h3/text()').getall()
        self.data["heading 4"] = response.xpath('//h4/text()').getall()
        self.data["other"] = (
            str(response.xpath('//rs-layer/text()').getall()))
        return self.data
