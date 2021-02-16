
import scrapy


class MyscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    writer = scrapy.Field()
    preview = scrapy.Field()

