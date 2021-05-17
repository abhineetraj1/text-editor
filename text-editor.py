from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
import os
import shutil as sl
def save_file():
	mn= sd.askstring("Save","Enter the filename")
	sl.copy(os.listdir()[0],mn)
	open(mn,"w").write(ed.get("1.0",END))
	msg.showinfo("Save","Your file is saved")
def open_file():
	mn= sd.askstring("Open","Enter the filename")
	open(mn,"r+").read()
	ed.insert(END,open(mn,"r+").read())
top=Tk()
top.title("Text Editor")
top.geometry("400x400")
ed = Text(font="28")
btn1= Button(command=save_file , font="28",text="Save",activebackground="black",background="white",activeforeground="white")
btn2= Button(command=open_file , font="28",text="Open",activebackground="black",background="white",activeforeground="white")
ed.place(x=0,y=50)
btn1.place(x=0,y=0)
btn2.place(x=100,y=0)
top.mainloop()