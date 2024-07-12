# scrapy_link_extractor.py
import scrapy
from scrapy.linkextractors import LinkExtractor


class QuoteSpider(scrapy.Spider):
	name = "OuoteSpider"
	start_urls = ["http://www.ime.eb.mil.br/"]

	def parse(self, response):
		link_extractor = LinkExtractor()
		links = link_extractor.extract_links(response)

		for link in links:
			yield {"url": link.url, "text": link.text}
