# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImbdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    
    durations = scrapy.Field()
    movie_ratings = scrapy.Field()
    movie_titles = scrapy.Field()
    movie_year = scrapy.Field()

