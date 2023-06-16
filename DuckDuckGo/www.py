import requests, json, re, time
from bs4 import BeautifulSoup
from urllib.parse import unquote
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
from requests.exceptions import ConnectionError

# Still have to make test and run some debugging

class ExternalCrawling:

    def __init__(self):
        self.keywords = []
        self.urls = []
        self.pattern = r"uddg=([^/]+)(?=%2F)|^(http|https)://"

    def setupEnvironment(self):

        with open("DuckDuckGo/KeyWords/commonKeywords2.json") as wordfile:
            data = json.load(wordfile)
            for word in data['keywords']:
                self.keywords.append(word)
    
    """
    To ensure that the proxy IP changes for each request, 
    we establish a new connection through the Tor network 
    for each request. This can be done by resetting the 
    Tor circuit before making each request.
    """
    def switchProxyIP(self):

        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

    def parseData(self,response):

        soup = BeautifulSoup(response.text,'html.parser')
        result_links = soup.find_all("a", class_="result__url")
        top_links = [link["href"] for link in result_links]
        return top_links
    
    def writeJson(self):

        data = {
            "urls:":self.urls
        }
        with open('DuckDuckGo/Urls/commonUrls2.json','w',encoding='utf-8') as file:

            #The indent=4 argument is optional and adds indentation to the JSON file for better readability
            json.dump(data,file, ensure_ascii=False, indent=4)

    def proxyRequest(self):

        self.setupEnvironment()
        count = len(self.keywords)
        for keyword in self.keywords:

            # Configure requests to use the proxy server and the random user agent
            proxies = {
                'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050'
            } 
            headers = {'User-Agent': UserAgent().random}

            url = f'https://duckduckgo.com/html/?q={keyword}'
            #for test
            count -= 1
            print(count)

            startTime = time.time()
            flag = True
            while flag:
                try:

                    self.switchProxyIP()
                    response = requests.get(url,proxies=proxies,headers=headers)
                    urls = self.parseData(response)
                
                    for url in urls:
                        #for test
                        print(url)

                        match = re.search(self.pattern, url)
                        if match is not None:
                            
                            if url.startswith('http://') or url.startswith('https://'):
                                self.urls.append(match.string)
                                flag = False
                            else:
                                extracted_url = match.group(1)
                                self.urls.append(unquote(extracted_url))
                                flag = False  

                    currentTime = time.time()
                    elapsedTime = currentTime - startTime

                    # If this while cycle takes more than 10 seconds to execute, it breaks it self
                    if elapsedTime > 10:
                        print("took more than 10 seconds")
                        flag = False

                # Handle the error or take appropriate action
                except (ConnectionError, requests.exceptions.ProxyError, requests.exceptions.Timeout) as e:
                    #melhorar isto
                    print("Entrou na exception, PoC !!!!!")

        self.writeJson()


if __name__ == "__main__":

    test = ExternalCrawling()
    test.proxyRequest()