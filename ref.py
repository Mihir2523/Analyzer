from pyt import *
from tkinter import *
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from tkinter import messagebox,ttk
	

def draw(file):
	def all(file):
		df = pd.read_csv(file)
		sns.pairplot(df,hue=str(drop2.get()),palette='plasma')
		plt.savefig("AllGraph.pdf",dpi=3000)
		messagebox.showinfo(title="Success",message="PDF Created Successfully")
		plt.show()
	
	root2 = Tk()
	root2.title("Choose Type Of Graph")
	root2.config(bg='light grey')
	root2.minsize(500,500)
	root2.maxsize(500,500)
	root2.resizable(False,False)
	
	df = pd.read_csv(file)
	a = list(df.columns)
	l = Label(root2,text="Choose Plotting Graph Style",font=('Consolas',16,'bold'))
	l2 = Label(root2,text="Choose Hue For All graph",font=('Consolas',10,'bold'))
	
	b1 = Button(root2,text="1.Scatter Plot",font=('Consolas',14,'bold'),command=lambda:plot(file,"ScatterPlot"))
	b2 = Button(root2,text="2.Bar Graph",font=('Consolas',14,'bold'),command=lambda:plot(file,"BarPlot"))
	b3 = Button(root2,text="3.Strip Plot",font=('Consolas',14,'bold'),command=lambda:plot(file,"StripPlot"))
	b4 = Button(root2,text="4.Violin Plot",font=('Consolas',14,'bold'),command=lambda:plot(file,"ViolinPlot"))
	
	b5 = Button(root2,text="5.Box Plot",font=('Consolas',14,'bold'),command=lambda:plot(file,"BoxPlot"))
	
	b6 = Button(root2,text="6.Cat Plot",font=('Consolas',14,'bold'),command=lambda:plot(file,"CatPlot"))
	b7 = Button(root2,text="7.All Above",font=('Consolas',14,'bold'),command=lambda:all(file))
	drop2 = ttk.Combobox(root2,values=a)
    
	l.place(x=100,y=40)
	b1.place(x=170,y=100)
	b2.place(x=170,y=150)
	b3.place(x=170,y=200)
	b4.place(x=170,y=250)
	b5.place(x=170,y=300)
	b6.place(x=170,y=350)
	b7.place(x=170,y=400)
	l2.place(x=310,y=400)
	drop2.place(x=310,y=430)
	root2.mainloop()
	