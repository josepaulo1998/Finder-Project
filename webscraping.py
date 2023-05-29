import urllib3
from urllib.request import urlopen, Request
import io, re
from bs4 import BeautifulSoup
import requests

def httpRequest():
  
    #Extracts all the HTML page
    
    #PoolManager instance for sending requests
    http = urllib3.PoolManager()

    #Sending a GET request
    resp = http.request("GET","https://totalsportek.pro/", preload_content=False)
    resp.auto_close = False

    myfile = open('C:/Trabalho/Projects/Walktrough/Finder/sportek.html','w')
    for line in io.TextIOWrapper(resp):
        myfile.write(line)
    myfile.close()
    