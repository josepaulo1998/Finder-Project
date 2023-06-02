#ProxyScrape
#delays between requests, rotating user agents, 
#using proxy servers to distribute requests
#https://www.youtube.com/watch?v=SFbV7sTSAlA
import requests

def test_proxy(proxy):
    try:
        response = requests.get("https://www.youtube.com", proxies={"http": proxy, "https": proxy}, timeout=10)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False

proxies = []
count = 0
with open("ProxySetting/http_proxies.txt","r") as file:
    for proxy in file:
        proxies.append(proxy)

for proxy in proxies:
    if test_proxy(proxy):
        print(f"Proxy {proxy} is working")
        with open("ProxySetting/http_proxies_valid.txt","a") as file:
            file.write(proxy)
    else:
        print(f"Proxy {proxy} is not working")