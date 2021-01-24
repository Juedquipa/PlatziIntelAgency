import scrapy

# Links //div[@class="field-item even"]/*[self::h2 or self::h3]/a/@href
# Doctitles //h1[@class="documentFirstHeading"]/text()
# Docp //div[@class="field-item even"]//p[not(@class)]/text()

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
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').getall()

        yield{
            'url': link,
            'tittle': title,
            'body': paragraph
        }
