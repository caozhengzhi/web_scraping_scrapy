
import scrapy

from scrapy import Item, Field

class WikiItem(Item):
    film = Field()
    year = Field()
    awards = Field()
    nominations = Field()
