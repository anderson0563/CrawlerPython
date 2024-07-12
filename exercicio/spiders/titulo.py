import scrapy


class QuotesSpider(scrapy.Spider):
    name = "titulo"
    start_urls = [
        'https://intraime.ime.eb.br/',
    ]

    def parse(self, response):
        for title in response.css('span.title'):
            yield {
                'title': title.css('span.title::text').get(),
            }