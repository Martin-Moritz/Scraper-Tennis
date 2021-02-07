# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Classement ATP - singles
class SinglesItem(scrapy.Item):
    rang = scrapy.Field()
    pays = scrapy.Field()
    joueur = scrapy.Field()
    age = scrapy.Field()
    points = scrapy.Field()
    tournois joues = scrapy.Field()

# Classement ATP - doubles
class DoublesItem(scrapy.Item):
    rang = scrapy.Field()
    pays = scrapy.Field()
    joueur = scrapy.Field()
    age = scrapy.Field()
    points = scrapy.Field()
    nb_tournois = scrapy.Field()
