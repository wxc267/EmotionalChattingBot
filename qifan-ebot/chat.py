import os
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
##from tkinter.constants import *
import wc

##import emoji
##from emoji import emojize

def robot_emoji(cond,emo_list):
        try:
                if cond == 0:
                        remo = Image.open("./remoji/init.jpg").resize((200,200),Image.ANTIALIAS)
                        remo = ImageTk.PhotoImage(remo)
                        rm.config(image = remo)
                        rm.image = remo
                elif cond == 1:
                        max_emo = ""
                        max_emov,count = 0,0
                        basic_emo = ['a','d','f','j','s']
                        for i in emo_list:
                                if i > max_emov:
                                        max_emov = i
                                        max_emo = basic_emo[count]
                                count += 1

                        if max_emo == "":
                                img_path = "./remoji/sorry.jpg"
                        else:
                                if max_emo == 'a':
                                        if max_emov < 0.5:
                                                img_path = "./remoji/anger1.jpg"
                                        elif max_emov < 0.75:
                                                img_path = "./remoji/anger2.jpg"
                                        else:
                                                img_path = "./remoji/anger3.jpg"
                                if max_emo == 'd':
                                        if max_emov < 0.50:
                                                img_path = "./remoji/disgust1.jpg"
                                        elif max_emov < 0.75:
                                                img_path = "./remoji/disgust2.jpg"
                                        else:
                                                img_path = "./remoji/disgust3.jpg"
                                if max_emo == 'f':
                                        if max_emov < 0.50:
                                                img_path = "./remoji/fear1.jpg"
                                        elif max_emov < 0.75:
                                                img_path = "./remoji/fear2.jpg"
                                        else:
                                                img_path = "./remoji/fear3.jpg"
                                if max_emo == 'j':
                                        if max_emov < 0.50:
                                                img_path = "./remoji/joy1.jpg"
                                        elif max_emov < 0.75:
                                                img_path = "./remoji/joy2.jpg"
                                        else:
                                                img_path = "./remoji/joy3.jpg"
                                if max_emo == 's':
                                        if max_emov < 0.50:
                                                img_path = "./remoji/sad1.jpg"
                                        elif max_emov < 0.75:
                                                img_path = "./remoji/sad2.jpg"
                                        else:
                                                img_path = "./remoji/sad3.jpg"
                        
                        remo = Image.open(img_path).resize((200,200),Image.ANTIALIAS)
                        remo = ImageTk.PhotoImage(remo)
                        rm.config(image = remo)
                        rm.image = remo
        except:
                print "Unexpected error:", sys.exc_info()[0]

def callback(event):
        if e.get():
                R.config(state=NORMAL)

                R.tag_configure('tag-right', justify='right')

                in_str = e.get()
                emo_lis = wc.emo_ana(in_str)
                R.image_create('insert',image = h_avt)
                R.insert('end',' ' + in_str + "\n") # This is the text you may want to use later

                robot_emoji(1,emo_lis)
                R.image_create('insert',image = r_avt)
                R.insert(END," Sorry, I don't know what you talking about\n")

                R.config(state=DISABLED)
                e.delete(0,END);
        return 0

master = Tk()

#################### Remoji ####################
newWindow = tk.Toplevel(master)
rm = tk.Label(newWindow)
robot_emoji(0,[])
rm.pack()
rname = "Rob"
################################################

e = Entry(master,width=80)
e.focus_set()
R = Text(master,height=30,width=100)
R.config(state=DISABLED)
R.pack(fill=BOTH,expand=1)
e.pack(fill=BOTH,expand=1,side=LEFT)
b = Button(master, text = "Send", width = 10, command = callback)
master.bind('<Return>', callback)
b.pack(side=LEFT)

#################### Avatar ####################
rmg = Image.open("r.jpg").resize((50,50),Image.ANTIALIAS)
hmg = Image.open("h.jpg").resize((50,50),Image.ANTIALIAS)
r_avt = ImageTk.PhotoImage(rmg)
h_avt = ImageTk.PhotoImage(hmg)
################################################

#################### Init Conversation ####################
R.config(state=NORMAL)
R.image_create('insert',image = r_avt)
R.insert(END," Hi, I am " + rname + ", nice to meet you!\n")
R.config(state=DISABLED)
###########################################################

mainloop()
