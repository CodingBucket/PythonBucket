# This is a chatbot program

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']]
]

chat = Chat(pairs, reflections)
chat.converse()