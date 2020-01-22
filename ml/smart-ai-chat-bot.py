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
print(string.punctuation)
print(remove_punct_dict)

# Create a function to return a list of lemmatized lower case words after removing punctuations
def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

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


# Generate the response
def response(user_response):
  
  # Question 'What is chronic kidney disease'

  user_response = user_response.lower() #Make the response lower case
  robo_response = ''

  # Append the users response to the sentence list
  sent_tokens.append(user_response)

  # Create a TfidfVectorizer Object
  TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words='english')

  # Convert the text to a matrix of TF-IDF features
  tfidf = TfidfVec.fit_transform(sent_tokens)

  # Get the measure of similarity (similarity scores)
  vals = cosine_similarity(tfidf[-1], tfidf)

  # Get the index of the most similar text/sentence to the users response
  idx = vals.argsort()[0][-2]

  # Reduce the dimensionality of vals
  flat = vals.flatten()

  # Sort the list in ascending order
  flat.sort()

  # Get the most similar score to the users response
  score = flat[-2]

  # If the variable 'score' is 0 then their is no text similar to the users response
  if(score == 0):
    robo_response = robo_response+"I apologize, I don't understand."
  else:
    robo_response = robo_response+sent_tokens[idx]
  
  # Remove the users response from the sentence tokens list
  sent_tokens.remove(user_response)
  
  return robo_response



flag = True
print("DOCBot: I am Doctor Bot or DOCBot for short. I will answer your queries about Chronic Kidney Disease. If you want to exit, type Bye!")
while(flag == True):
  user_response = input()
  user_response = user_response.lower()
  if(user_response != 'bye'):
    if(user_response == 'thanks' or user_response =='thank you'):
      flag=False
      print("DOCBot: You are welcome !")
    else:
      if(greeting(user_response) != None):
        print("DOCBot: " + greeting(user_response))
      else:
        print("DOCBot: " + response(user_response))       
  else:
    flag = False
    print("DOCBot: Chat with you later !")