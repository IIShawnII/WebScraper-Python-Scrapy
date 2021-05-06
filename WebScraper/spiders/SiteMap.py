from scrapy.spiders import SitemapSpider

class SitemapSpider(SitemapSpider):
    name = 'SiteMap'
    sitemap_urls = ['http://cochranetel.ca/wp-sitemap.xml']
    allowed_domains = ['cochranetel.ca']

    def parse(self, response):
        filename = 'All-Texts.txt' 
        with open(filename, mode='a', encoding='UTF-8') as f: 
            f.write("Page: (")
            f.write(response.url)
            f.write(")\r\n#######################################################################################################")
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
            f.write("End\r\n#######################################################################################################")
            f.write("\r\n")
