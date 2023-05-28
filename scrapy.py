#https://www.youtube.com/watch?v=QdLgNr1mKQU
import scrapy
import re

class MySpider():

    name = 'myspider'

    start_urls = ['https://totalsportek.pro/']

    def parse(self, response):
        print('url:', response.url)

        for pattern in ['view', '\\bviews\\b', '\d+ views']:
            print('>>> pattern:', pattern)

            result = re.findall(pattern, response.text) 
            print('>>>          re:', len(result), result[0:3])

            result = response.css('body').re(pattern)
            print('>>> response.re:', len(result), result[0:3])

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
c.crawl(MySpider)
c.start()