import nltk
from newspaper import Article
url = input("Article URL: ")
article = Article(url)
article.download()
article.parse()
article.nlp()
print(article.summary)
text = article.text
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(text)['compound'])
