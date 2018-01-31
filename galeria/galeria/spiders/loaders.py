# -*- coding: utf-8 -*-

import datetime
import scrapy
from galeria.items import GaleriaItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.http import Request


class BasicSpider(scrapy.Spider):
    name = 'prawie'
    start_urls = [#'http://galeriazyskow.pl/kategoria/analizy/',
                  #'http://galeriazyskow.pl/kategoria/aktualnosci/',
                  #'http://galeriazyskow.pl/kategoria/analizy-akcji/',
                  #'http://galeriazyskow.pl/kategoria/analizy-wideo/',
                  #'http://galeriazyskow.pl/kategoria/ekonomia/',
                  'http://galeriazyskow.pl/kategoria/forex/',
                  #'http://galeriazyskow.pl/kategoria/komentarze-gieldowe/',
                  #'http://galeriazyskow.pl/kategoria/polecane/',
                  #'http://galeriazyskow.pl/kategoria/systemy-na-glownej/',
                 ]

    def parse(self, response):
        for post_url in response.css('div.post-image > a ::attr(href)').extract():
            yield scrapy.Request(response.urljoin(post_url), callback=self.parse_post)
        next_page = response.css('a.next.page-numbers ::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_post(self, response):
        """
        This function parses a post page.
        
        @url http://galeriazyskow.pl/dolar-zlapal-zadyszke-30-01-2018r/
        @url http://galeriazyskow.pl/pln-pod-lekka-presja-dane-dot-pkb-w-kalendarzu-30-01-2018r/
        @returns items 1
        @scrapes text
        """
        l = ItemLoader(item=GaleriaItem(), response=response)

        l.add_xpath('text', '//div[@class="entry-content"]//text()[re:test(., "\w+")]')#, MapCompose(str.strip))

#        l.add_value('url', response.url)
#        l.add_value('date', datetime.datetime.now())
        yield l.load_item()

