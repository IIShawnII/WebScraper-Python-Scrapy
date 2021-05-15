import scrapy


class SinglePageSpider(scrapy.Spider):
    name = 'SinglePage'
    allowed_domains = ['cochranetel.ca']
    start_urls = ['https://cochranetel.ca/']

    def parse(self, response):
        
        filename = 'test.txt' 
        with open(filename, mode='a', encoding='UTF-8') as f: 
            f.write(response.url)
            f.write("\r\n")
            f.write(str(response.xpath('//title/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//a/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//span/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//p/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//strong/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//h1/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//h2/text()').getall()))
            f.write("\r\n")
            f.write(str(response.xpath('//rs-layer/text()').getall()))
            f.write("\r\n")
