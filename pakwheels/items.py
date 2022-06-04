# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PakwheelsList(scrapy.Item):
    items = scrapy.Field()


class PakwheelsItem(scrapy.Item):
    listing_id = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    fuel_type = scrapy.Field()
    cc = scrapy.Field()
    transmission = scrapy.Field()
    price = scrapy.Field()
