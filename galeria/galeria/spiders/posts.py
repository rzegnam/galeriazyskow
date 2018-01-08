import scrapy
from scrapy.loader import ItemLoader
from galeria.items import GaleriaItem


class PostSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        "http://galeriazyskow.pl/analiza-usdpln-1d/"
    ]

    def parse(self, response):
        for parag in response.css('div.entry-content'):
            yield {
                        'text': ' '.join(parag.css('::text').re(r'\w+')), #   STRING trzeci - uproszczony - tylko litery
            }

#            next_page = response.css('div.nav-next a::attr(href)').extract_first()     CSS way
        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



# xpath do linkow
#'link': response.xpath('//link[@rel="canonical"]/@href').extract_first()
# pierwszy selector
#'text': parag.css('p::text').re(r'\w+'),
# drugi selector
# 'text': ' '.join(parag.css('p::text').re(r'\w+')), #   STRING
# trzeci selektor - tylko litery
# 'text': ' '.join(parag.css('::text').re(r'\w+')), #   STRING
# czwarty, trzeba dopracowac re?
#'text': parag.xpath('.//text()[re:test(., "\w+")]').extract(), #