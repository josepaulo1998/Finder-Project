import scrapy


class TotalsportekSpider(scrapy.Spider):
    name = "totalsportek"
    start_urls = ["https://totalsportek.pro/"]

    def parse(self, response):
        games = response.css('.nav-link2')
        timeremaining2start = response.css('.Aj::text')
        teamname = response.css('.col-11::text')

        pass
