# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://galeriazyskow.pl/analiza-usdpln-1d/']

    def parse(self, response):
        parag = response.css('div.entry-content')
        self.log("tekst: %s" % ' '.join(parag.css('::text').re(r'\w+')))
