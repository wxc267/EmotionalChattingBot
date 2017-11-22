from tkinter import *
from nltk import word_tokenize
import random
from chatterbot import ChatBot

def get_response(input_str):
	response = bot.get_response(input_str)
	return response

def callback():
	input_str = e.get()

	if input_str:
		T.config(state=NORMAL)
		T.insert(END,"You: ")
		T.insert(END,input_str)
		T.insert(END,"\n")
		T.insert(END,bot.name + ": ")
		T.insert(END,get_response(input_str))
		T.insert(END,"\n")
		T.config(state=DISABLED)	
		e.delete(0,END);

bot = ChatBot(
    "Ebot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.60,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer="chatterbot.trainers.ChatterBotCorpusTrainer",
    database="database.sqlite"
)

bot.train("data")

master = Tk()
e = Entry(master,width=80)
e.focus_set()
T=Text(master,height=30,width=100)
T.config(state=DISABLED)
T.pack(fill=BOTH,expand=1)
e.pack(fill=BOTH,expand=1,side=LEFT)
b = Button(master, text = "Send", width = 10, command = callback)
b.pack(side=LEFT)

mainloop()
