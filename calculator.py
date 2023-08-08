import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root=tk.Tk()
root.geometry('550x300+222+222')
root.title('calculator')
a=tk.StringVar()
b=tk.StringVar()


    
frm2=ttk.Frame(root)
frm2.pack(ipadx=20,ipady=20,padx=5,pady=5,expand=False)    

frm1=ttk.Frame(root)
frm1.pack()

frm3=ttk.Frame(root)
frm3.pack(fill=tk.X)



tbox1=ttk.Entry(frm2,textvariable=a).grid(row=0,column=0)
tbox2=ttk.Entry(frm2,textvariable=b).grid(row=0,column=4,ipadx=2)
tbox5=ttk.Label(frm2,font=('Arial',16))
tbox5.grid(row=0,column=2,ipadx=8)


a.get()
b.get()

label=ttk.Label(frm2,text='   ').grid(row=0,column=1,pady=2)

btn1=ttk.Button(master=frm1,text='+',command=lambda: select('add'))
btn1.grid(row=0,column=0)

btn2=ttk.Button(master=frm1,text='- ',command=lambda: select('sub'))
btn2.grid(row=0,column=1)

btn5=ttk.Button(master=frm1,text='CLEAR',command=lambda: select('clr'))
btn5.grid(row=2,columnspan=4)

btn3=ttk.Button(master=frm1,text='*',command=lambda: select('mult'))
btn3.grid(row=1,column=0)

btn3=ttk.Button(master=frm1,text='/',command=lambda: select('div'))
btn3.grid(row=1,column=1)

tbox4=ttk.Label(frm3,text='Result :').grid(row=0,column=0)
tbox3=tk.Label(frm3)
tbox3.grid(row=0,column=2)

def select(option):
    result=0
    if option=='add':
        
        result=int(a.get())+int(b.get())
        tbox5.config(text='+')
        
    elif option=='sub':
        tbox5.config(text='-')
        result=int(a.get())-int(b.get())
        
    elif option=='mult':
        tbox5.config(text='*')
        result=int(a.get())*int(b.get())
        
    elif option=='div':
        tbox5.config(text='÷')
        result=int(a.get())/int(b.get())
        
    elif option=='clr':
        result=""
        tbox5.config(text="")

    tbox3.config(text=f"{result}")   

root.mainloop()
