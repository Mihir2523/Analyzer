from singel import *
from ref import *
import pandas as pd
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import webbrowser
import os

file=" "
global df
global col

df = None
col = None
def chatbot():
	pathh = f'''file:///{os.getcwd().replace("\\","/")}/demo.html'''
	webbrowser.open(pathh)
def path():
	global file
	global df 
	file = filedialog.askopenfilename(initialdir="C:",title="Choose CSV File")
	df = pd.read_csv(file)
	col = list(df.columns)

root = Tk()

root.geometry("1000x550")
root.title("Analyzer")
root.resizable(False,False)
i = Image.open("brand.jpg")
i = i.resize((1000,550))
img = ImageTk.PhotoImage(i)

bgg = Label(root,image=img)
l = Label(root,text="Step 1.Select A File"
	,font=("Consolas",18,'bold'),bg='light grey',fg='black')
b = Button(root,text="=> Select",font=("Consolas",18,'bold'),bg='grey',fg='black',command=path)
m = Label(root,text="Welcome To Analyzer",font=("Consolas",22,'bold'),bg='light blue',fg='red')
l2 = Label(root,text="Step 2.Analysis Type"
	,font=("Consolas",18,'bold'),bg='light grey',fg='black')
b2 = Button(root,text="=> Single-Column(NUMERIC ONLY)",font=("Consolas",14,'bold'),bg='grey',fg='black',command=lambda : single(file))
b3 = Button(root,text="=> Multi-Columns(GRAPHS)",font=("Consolas",15,'bold'),bg='grey',fg='black',command=lambda:draw(file))
b4 = Button(root,text="HELP",font=("Consolas",15,'bold'),bg='grey',fg='black',command=chatbot)


bgg.place(relheight=1,relwidth=1)
m.place(x=350,y=20)
l.place(x=50,y=200)
b.place(x=50,y=300)
l2.place(x=670,y=200)
b2.place(x=670,y=300)
b3.place(x=670,y=400)
b4.place(x=470,y=480)
root.mainloop()

