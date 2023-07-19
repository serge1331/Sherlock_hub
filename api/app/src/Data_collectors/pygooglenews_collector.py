from pygooglenews import GoogleNews
from datetime import datetime
import time



def collect(keyword , country="BJ" , language="fr"):
    news = []
    gn = GoogleNews(lang=language , country=country )
    search = gn.search(keyword)
    articles = search['entries']
    for i in articles: 
        article = {'opinion': i.title  , 'link': i.link , 'published': i.published}
        news.append(article)
    return news