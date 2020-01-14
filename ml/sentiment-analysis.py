# Get the sentiment of text from a website

# pip install newspaper3k textblob

# Import the libraries
from textblob import TextBlob
import nltk
from newspaper import Article

# Get the article
url = 'https://stackoverflow.com/'
article = Article(url)

# Natural Language Processing
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# Get the summary of the article
text = article.summary
print(text)

# Create a TextBlob object
obj = TextBlob(text)

# This returns a value between -1 and 1
sentiment = obj.sentiment.polarity
print(sentiment)

if sentiment == 0:
    print('The text is neutral')
elif sentiment > 0:
    print('The text is positive')
else:
    print('The text is negative')
