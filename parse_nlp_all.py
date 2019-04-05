import paralleldots
from newspaper import Article
import getURLs

paralleldots.set_api_key("VkuigAku4meDwQPFy0uHHxRZilBTSTQuu9PEmLMAOas")
lang_code = "en"

def score(ticker):
    FYPapers = getURLs.urls(ticker)
    count = 0
    score = 0
    for url in FYPapers:
        article = Article(url)
        count += 1
        article.download()
        article.parse()
        text = article.text
        response = paralleldots.sentiment(text, lang_code)["sentiment"]
        score += ((response["positive"] - response["negative"])*(1-response["neutral"]))
    return (score/count)
