import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox,ttk

def plot(path,type):
    df = pd.read_csv(path)
    a = list(df.columns)
    st1 = None
    st2 = None
    def a2():
        nonlocal st1
        if lst1.curselection()==():
            messagebox.showerror(title='First Column Not Found',message='Please Select column first')
        else:
            st1 = lst1.get(lst1.curselection())

    def c2():
        nonlocal st2
        if lst2.curselection()==():
            messagebox.showerror(title='Second Column Not Found',message='Please Select column first')
        else:
            st2 = lst2.get(lst2.curselection())

    def sub():
        nonlocal st1
        nonlocal st2
        nonlocal df
        if st1 is None or st2 is None:
             messagebox.showerror(title='Select Columns',message='Please Select columns first')
        else:
            if type=='ScatterPlot':
                b = sns.scatterplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='Accent')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                plt.show()
            elif type == 'BarPlot':
                b=sns.barplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='plasma',orient='v')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.show()
            elif type == 'StripPlot':
                b=sns.stripplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='plasma')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.show()
            elif type == 'ViolinPlot':
                b=sns.violinplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='flare')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.show()
            elif type == 'BoxPlot':
                b=sns.boxplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette="rocket_r")
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.show()
            elif type == 'CatPlot':
                b=sns.catplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette="Oranges")
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.show()
            else:
                 messagebox.showinfo(title="In Future",message="We will Notify When Feature Comes")          
    
    def save():
        nonlocal st1
        nonlocal st2
        nonlocal df 
        
        if st1 is None or st2 is None:
             messagebox.showerror(title='Select Columns',message='Please Select columns first')
        else:
            if type == 'ScatterPlot':
                b = sns.scatterplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='Accent')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                b.set_xlabel(str(st1),fontsize=10)
                plt.savefig("ScatterGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            elif type == 'BarPlot':
                b = sns.barplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='plasma',orient='v')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.savefig("BarGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            elif type == 'StripPlot':
                b = sns.stripplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='plasma')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.savefig("StripGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            elif type == 'ViolinPlot':
                b = sns.violinplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette='flare')
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.savefig("ViolinGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            elif type == 'BoxPlot':
                b = sns.boxplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette="rocket_r")
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.savefig("BoxGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            elif type == 'CatPlot':
                b = sns.catplot(x=str(st1), y=str(st2), data=df,hue=str(drop1.get()),palette="Oranges")
                b.set_xticklabels(b.get_xticklabels(),rotation=90,horizontalalignment='right')
                
                plt.savefig("CatGraph.pdf",dpi=3500)
                messagebox.showinfo(title="Success",message="PDF Created Successfully")
            else:
                 messagebox.showinfo(title="In Future",message="We will Notify When Feature Comes")          
    root = Tk()
    root.title("GRAPHS")
    root.minsize(600, 500)
    root.maxsize(600, 500)
    root.config(bg='#40e0d0')
    root.resizable(False,False)

    drop1 = ttk.Combobox(root,values=a)
    
    name = Label(root, text='#' + str(type), font=('Arial', 20, 'bold'))
    l1 = Label(root, text='1. First Column', font=('Consolas', 15), fg='red')
    l2 = Label(root, text='2. Second Column', font=('Consolas', 15), fg='red')
    l3 = Label(root, text='3. Hue', font=('Consolas', 15), fg='red')

    scb1 = Scrollbar(root, orient=VERTICAL)
    scb2 = Scrollbar(root, orient=VERTICAL)
    
    lst1 = Listbox(root, yscrollcommand=scb1.set, font=('Consolas', 12, 'bold'), bg='#f7ffde', fg='black', width=10,height=6)
    for i in range(len(a)):
        lst1.insert(i, a[i])

    lst2 = Listbox(root, yscrollcommand=scb2.set, font=('Consolas', 12, 'bold'), bg='#f7ffde', fg='black', width=10,height=6)
    for i in range(len(a)):
        lst2.insert(i, a[i])

    scb1.config(command=lst1.yview)
    scb2.config(command=lst2.yview)

    a1 = Button(root, text='Select First', bg='yellow', fg='red', width=10, height=3, command=a2)
    c1 = Button(root, text='Select Second', bg='yellow', fg='red', width=10, height=3, command=c2)
    b = Button(root, text=type, bg='black', fg='white', width=18, height=3, command=sub)
    save = Button(root, text='Save As PDF', bg='black', fg='white', width=18, height=3, command=save)

    name.place(x=60, y=30)
    l1.place(x=100, y=100)
    l2.place(x=100, y=250)

    lst1.place(x=300, y=100)
    lst2.place(x=300, y=250)
    b.place(x=250, y=420)
    save.place(x=400, y=420)
    l3.place(x=50,y=380)
    a1.place(x=450, y=100)  
    c1.place(x=450, y=250)  
    scb1.place(x=310,y=100)
    scb2.place(x=310,y=250)
    drop1.place(x=50,y=420)
    root.mainloop()