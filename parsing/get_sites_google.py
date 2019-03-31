links = []
from googlesearch import search

# to search

query = input("query: ")

query += " site:https://finance.yahoo.com/news/"

for j in search(query, tld="co.in", num=10, stop=None, pause=2):
    links.append(j)
    print(j)
