import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

choice=None
def single(file):
	df = pd.read_csv(file)
	a = list(df.columns)
	def sav(parm):
		global choice
		nonlocal df 
		nonlocal a 
		choice = drop.get()
		if(parm == "hist"):
			b = sns.displot(df[str(choice)],kde=True,rug=True)
			b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
			plt.savefig('Histogram.pdf',dpi=2500)	
		else:
			b = sns.countplot(x=str(choice),data = df)
			b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
			plt.savefig('Count Plot.pdf',dpi=2500)
		messagebox.showinfo(title="Success",message="PDF Created Successfully")
           

	def count():
		nonlocal df 
		nonlocal a 
		
		global choice
		choice = drop.get()
		sns.countplot(x=str(choice),data = df)
		plt.show()
	def hist():
		nonlocal df 
		nonlocal a 
		
		global choice
		choice = drop.get()
		sns.displot(df[str(choice)],kde=True,rug=True)
		plt.show()
	def num():
		nonlocal df 
		nonlocal a 
		
		global choice
		choice = drop.get()
		lst = np.array(list(df[str(choice)]))
		
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)
		
		e1.insert(0,str(lst.max()))

		e2.insert(0,str(lst.min()))

		e3.insert(0,str(lst.sum()/len(lst)))

		e4.insert(0,str(lst.sum()))

		e5.insert(0,str(lst.std()))

	root1 = Tk()
	root1.minsize(1000,500)
	root1.title("Single Column Analysis")
	root1.maxsize(1000,500)
	root1.config(bg="#faebd7")

	root1.resizable(False,False)
	l = Label(root1,text="Select Numeric Column",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	l1 = Label(root1,text = "Max Element Form Data : ",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')

	l2 = Label(root1,text = "Min Element Form Data : ",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	
	l3 = Label(root1,text = "Average Of Data : ",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	
	l4 = Label(root1,text = "Sum OF Data : ",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	
	l5 = Label(root1,text = "Standard Deviation : ",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	l6 = Label(root1,text = "GRAPHS",font=("Consolas",14,'bold'),fg='#800000',bg='#cccccc')
	l7 = Label(root1,text = "- Count Plot is For counting Number of occurence ",font=("Consolas",10,'bold'),fg='#800000',bg='#cccccc')
	l8 = Label(root1,text = "- Ex- Count No of Male and Female",font=("Consolas",10,'bold'),fg='#800000',bg='#cccccc')
	
	e1 = Entry(root1,font=('Consolas',15,'bold'),bg='light grey',fg = 'black')
	e2 = Entry(root1,font=('Consolas',15,'bold'),bg='light grey',fg = 'black')
	e3 = Entry(root1,font=('Consolas',15,'bold'),bg='light grey',fg = 'black')
	e4 = Entry(root1,font=('Consolas',15,'bold'),bg='light grey',fg = 'black')
	e5 = Entry(root1,font=('Consolas',15,'bold'),bg='light grey',fg = 'black')
	
	drop = ttk.Combobox(root1,values=a)
	drop.place(x=350,y=20)
	b = Button(root1,text="Calculate",font=("Consolas",12),fg='red',bg='dark grey',command=num)
	b1 = Button(root1,text="Histogram",font=("Consolas",12),fg='red',bg='dark grey',command=hist)
	b2 = Button(root1,text="Count Plot",font=("Consolas",12),fg='red',bg='dark grey',command=count)
	b3 = Button(root1,text="Save Histogram",font=("Consolas",12),fg='red',bg='dark grey',command=lambda : sav("hist"))

	b4 = Button(root1,text="Save CountPlot",font=("Consolas",12),fg='red',bg='dark grey',command=lambda : sav("count"))
	

	l.place(x=80,y=20)
	l1.place(x=80,y=100)
	l2.place(x=80,y=150)
	l3.place(x=80,y=200)
	l4.place(x=80,y=250)
	l5.place(x=80,y=300)
	b.place(x=510,y=20)
	e1.place(x=350,y=100)
	e2.place(x=350,y=150)
	e3.place(x=350,y=200)
	e4.place(x=350,y=250)
	e5.place(x=350,y=300)
	l6.place(x=800,y=50)
	l7.place(x=650,y=100)
	l8.place(x=650,y=150)
	b1.place(x=800,y=250)
	b2.place(x=800,y=300)
	b3.place(x=800,y=350)
	b4.place(x=800,y=400)
	root1.mainloop()