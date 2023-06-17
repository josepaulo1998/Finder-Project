import json
from collections import Counter

urls = []

with open("DuckDuckGo/Urls/popularUrls5.json") as file:
    data = json.load(file)

    for url in data["urls:"]:
        urls.append(url)


result = [{'url':key, 'count':value} for key,value in Counter(urls).items()]

with open("DuckDuckGo/Survey/popularSurveyUrls5.json","w",encoding='utf-8') as file:
    json.dump(result,file, ensure_ascii=False, indent=4)



