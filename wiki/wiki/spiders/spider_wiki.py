from scrapy import Spider
from scrapy.selector import Selector
from wiki.items import WikiItem

class WikiSpider(Spider):
    name = 'wiki_spider'
    allowed_urls = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films']

    def verify(self, content):
        if isinstance(content, list):
            if len(content) > 0:
                return content[0]
            else:
                return ""
        else:
            return content

    def parse(self, response):
        rows = response.xpath('//div[@id="mw-content-text"]/div/table/tr')
        patterns = ['./td[1]/i/a/text()', './td[1]/i/b/a/text()', './td[1]/i/span[2]//text()',
                    './td[1]/i/b/span/text()']
        for row in rows:

            for pattern in patterns:
                film = row.xpath(pattern).extract()
                # film = row.xpath(pattern).extract_first()
                film = self.verify(film)
                if film:
                    break
            year = row.xpath('./td[2]/a/text()').extract()
            year = self.verify(year)
            awards = row.xpath('./td[3]/text()').extract()
            awards = self.verify(awards)
            nominations = row.xpath('./td[4]/text()').extract()
            nominations = self.verify(nominations)

            item = WikiItem()
            item['film'] = film
            item['year'] = year
            item['awards'] = awards
            item['nominations'] = nominations
            yield item


