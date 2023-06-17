import json
from collections import Counter

urls = []

with open("DuckDuckGo/Urls/commonUrls5.json") as file:
    data = json.load(file)

    for url in data["urls:"]:
        urls.append(url)

a = Counter(urls)
a.most_common()
result = [{'url':key, 'count':value} for key,value in a.most_common()]

with open("DuckDuckGo/Survey/surveyUrls5.json","w",encoding='utf-8') as file:
    json.dump(result,file, ensure_ascii=False, indent=4)



