import scrapy
from scrapy_splash import SplashRequest

class Quotes2ScrapeSpider(scrapy.Spider):
	name = 'quotes2scrape'
	
	def start_requests(self):
		yield SplashRequest(
			url='http://quotes.toscrape.com/js/',
			callback=self.parse,
		)

	def parse(self, response):
		for quote in response.css("div.quote"):
			quote_text = quote.css("span.text::text").extract_first()
			quote_author = quote.css("small.author::text").extract_first()
			quote_tags = quote.css("div.tags > a.tag::text").extract()

			#Yield is used to map the values for output
			yield {
			'Quote': quote_text,
			'Author': quote_author,
			'Tags': quote_tags,
			}
			
		#This function is to navigate to the next page
		next_page = response.css("li.next > a::attr(href)").extract_first()
		if next_page is not None:
			yield SplashRequest(response.urljoin(next_page))