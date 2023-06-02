from googlesearch import search
import postgresqlConnection as db
import json, time

class ExternalCrawling:

    def __init__(self):
        self.keywords = []
        self.urls = []

    def addKeywords(self):
        for i in range(1,6):
            filename = f'GoogleSearch/KeyWords/popularKeywords{i}.json'
            with open(filename) as f:
                #Loads the file's content into data variables
                data = json.load(f)

                for words in data['keywords']:
                    self.keywords.append(words)

                self.addUrls()

    def addUrls(self):

        for word in self.keywords:
            self.urls.append(list(search(word, num_results=20)))
            time.sleep(7)

        self.writeFile()

    def writeFile(self):
        for i in range(1,6):
            filename = f'GoogleSearch/Urls/popularKeywords{i}.json'
            with open(filename, "w") as file:
                json.dump(self.urls, file)
                    
        """
        CONNECT WITH DATA BASE:
        for url in urls:
        db.PostgresqlDB.dbParseUrl(url)
        """

if __name__ == "__main__":

    test = ExternalCrawling()
    test.addKeywords()

