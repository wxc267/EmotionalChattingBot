from Tkinter import *



def callback():
	
	if e.get():
		T.config(state=NORMAL)
		T.insert(END,"You: ")
		T.insert(END,e.get()) # This is the text you may want to use later
		T.insert(END,"\n")
		T.config(state=DISABLED)
		e.delete(0,END);

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
