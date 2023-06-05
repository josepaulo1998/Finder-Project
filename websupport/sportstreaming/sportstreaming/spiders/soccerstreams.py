import scrapy


class SoccerstreamsSpider(scrapy.Spider):
    name = "soccerstreams"
    allowed_domains = ["www.redditsoccerstreams.tv"]
    start_urls = ["https://www.redditsoccerstreams.tv/"]

    def parse(self, response):

        for jogos in response.css('tr'):
            yield{
                'hora' : jogos.css('.et3::text').get(),
                'titulo' : jogos.css('.et4::text').get(),
                'link' : jogos.css('.et5 > a::attr(href)').get()
            }

        pass
