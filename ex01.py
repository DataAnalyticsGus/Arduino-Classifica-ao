import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

#text="Wow! The movie was amazing, I loved minute of it!"
text=" i go at the school every day, but i dont like!"

sia=SentimentIntensityAnalyzer()

sentiment=sia.polarity_scores(text)

print(sentiment)