import scrapy


class Craw_Spider(scrapy.Spider):
    name = 'get'

    start_urls = [
        """test pages"""
        'https://blog.scrapinghub.com/',
    ]
    pages_count = 2

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://blog.scrapinghub.com/{page}'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        for href in response.css('css-margin here').extact():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        techs = {}
        for row in response.css('crawling css type'):
            cols = row.css('td:text').extract()
            techs[cols[0]] = cols[1]