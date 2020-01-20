# This is a self learning chatbot program

from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Download the packages from NLTK
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Get the article URL
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
text = article.text

# Convert the text into a list of sentences
sent_tokens = nltk.sent_tokenize(text) 
print(sent_tokens)

# Create a dictionary (key:value) pair to remove punctuations
remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)

# Print the punctuations
print(string.punctuation)

# Print the dictionary
print(remove_punct_dict)

# Create a function to return a list of lemmatized lower case words after removing punctuations
def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

# Print the tokenization text
print(LemNormalize(text))


# Greeting Inputs
GREETING_INPUTS = ["hi", "hello", "hola", "greetings", "wassup", "hey"]

# Greeting responses back to the user
GREETING_RESPONSES=["howdy", "hi", "hey", "what's good", "hello", "hey there"]

# Function to return a random greeting response to a users greeting
def greeting(sentence):
  # if the user's input is a greeting, then return a randomly chosen greeting response
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_RESPONSES)