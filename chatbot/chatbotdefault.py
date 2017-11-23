# -*- coding: utf-8 -*-
#need to install chatterbot: pip install chatterbot
#this chatbot is trained by chatterbot corpus - https://github.com/gunthercox/chatterbot-corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ron Obvious") #"Ron Obvious" is the name of the chatbot

#training the chatbot with a conversation list
'''
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
'''
#the commented code above shows how to train a chatbot with conversations

#use the trained data in the exist libary
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train(
	"chatterbot.corpus.english.conversations",
	"chatterbot.corpus.english.emotion"
)

#get and print response from the chatbot
while True:
	input_conversation=raw_input("you:")
	response = chatbot.get_response(input_conversation)
	print("bot:")
	print(response)
