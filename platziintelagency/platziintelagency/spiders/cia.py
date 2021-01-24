import scrapy

# Links //div[@class="field-item even"]/*[self::h2 or self::h3]/a/@href

class SpiderCIA(scrapy.Spider):

    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]

    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        links_declassified = response.xpath('//div[@class="field-item even"]/*[self::h2 or self::h3]/a/@href').getall()
        for link in links_declassified:
            yield response.follow(link, callback=self.parse_link)

    def parse_link(self, response):
        pass
