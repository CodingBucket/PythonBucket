# Description: This program takes text from an online article and convert it to speech

# Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

# Get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

article.download() # Download the article
article.parse()   # Parse the article
nltk.download('punkt') # Download the punkt package
article.nlp() # Apply NLP (Natural Language Processing)

# Get the articles text and store it into a variable
mytext = article.text

print(mytext)

language = 'en'

# Convert text to speech
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the converted audio to a file
myobj.save('read_article.mp3')

# Play the audio file
os.system('start read_article.mp3')

