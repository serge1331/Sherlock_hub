from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer
from .Dataset_generator import DatasetGenerator as dsg
import time



def sentiment(sentence):
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	return sentiment_dict['compound']

"""===================================================================="""

def sentiment_dispatcher(sentiments):
	neg , pos =  0 , 0

	for sentiment in sentiments:
		if sentiment <= 0:
			neg += sentiment
		else:
			pos += sentiment
	
	yield neg
	yield pos


"""===================================================================="""

def result(keyword):
	gen = dsg(keyword)
	res =  gen.generator()
	res['sentiment'] = res['opinion'].apply(sentiment)
	
	neg , pos = sentiment_dispatcher(res['sentiment'])

	yield neg
	yield pos
	yield res['sentiment'].sum()
	yield res


