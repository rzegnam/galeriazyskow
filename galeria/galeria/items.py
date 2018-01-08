# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaleriaItem(scrapy.Item):
    text = scrapy.Field()
    # image_urls = scrapy.Field()
    # image= scrapy.Field()
    # pub_date = scrapy.Field()
    #
    # # Housekeeping fields
    # url = scrapy.Field()
    # project = scrapy.Field()
    # spider = scrapy.Field()
    # server = scrapy.Field()
    # date = scrapy.Field()