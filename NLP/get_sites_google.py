"""
import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)
"""

links = []

try:
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 

query = input("query: ")

query += " site:https://finance.yahoo.com/news/"

for j in search(query, tld="co.in", num=10, stop=None, pause=2): 
    links.append(j)
    print(j)