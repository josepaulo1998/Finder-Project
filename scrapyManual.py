from googlesearch import search
import postgresqlConnection as db

keyword = "Reddit Soccer Streams"
num_results = 20  # Number of search results to retrieve

urls = list(search(keyword, num_results=num_results))

#for url in urls:
#    db.PostgresqlDB.dbParseUrl(url)

with open("urls.txt", "w") as file:
    for url in urls:
        file.write(url + "\n")