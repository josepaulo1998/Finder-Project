#https://www.youtube.com/watch?v=QdLgNr1mKQU
#https://www.reddit.com/r/SoccerBetting/comments/xf0xk2/football_livestreaming_platform/
#https://stream2u.live/
#w8ting for aproval
import scrapy
import json
from scrapy.crawler import CrawlerProcess
from time import sleep, time

class RedditSpider(scrapy.Spider):
    name = "reddit_spider"
    start_time = None
    request_count = 0

    def start_requests(self):
        # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Reddit API credentials
        client_id = 'YOUR_CLIENT_ID'
        client_secret = 'YOUR_CLIENT_SECRET'
        keyword = 'futbol'

        # Obtain an access token from Reddit API
        auth_url = 'https://www.reddit.com/api/v1/access_token'
        headers = {'User-Agent': 'Mozilla/5.0'}
        data = {'grant_type': 'client_credentials'}
        response = scrapy.FormRequest(auth_url,method='POST',headers=headers,formdata=data,auth=(client_id, client_secret))

        yield response.follow(url='https://www.reddit.com/r/all/search.json?q=' + keyword,headers={'Authorization': f'Bearer {response.json()["access_token"]}'})
    
    def parse(self, response):
        if self.start_time is None:
            self.start_time = time()

        json_response = json.loads(response.body)

        # Extract the URLs from the search results
        posts = json_response['data']['children']
        for post in posts:
            url = post['data']['url']
            yield {
                'url': url
            }

        self.request_count += 1
        elapsed_time = time() - self.start_time
        if elapsed_time < 60 and self.request_count < 60:
            sleep(1)
        else:
            self.start_time = time()
            self.request_count = 0

# Run the spider
process = CrawlerProcess()
process.crawl(RedditSpider)
process.start()
