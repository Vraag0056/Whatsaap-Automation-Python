import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys

from threading import Thread


root = Tk()

root.title('Admin')
root.geometry('900x570')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="icon.ico")
Label(root,image=img,bg='white').place(x=50,y=120)

frame = Frame(root,width=350,height=480,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Admin Login', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=75,y=5)


Button(frame,width=39,pady=7,text = 'Subjects',bg='#57a1f8',fg='white',border=0).place(x=30,y=80)
Button(frame,width=39,pady=7,text = 'Faculty',bg='#57a1f8',fg='white',border=0).place(x=30,y=140)
Button(frame,width=39,pady=7,text = 'Add Timings',bg='#57a1f8',fg='white',border=0).place(x=30,y=200)
Button(frame,width=39,pady=7,text = 'Add Batch',bg='#57a1f8',fg='white',border=0).place(x=30,y=260)
Label(root,text='Created By : V-raag',bg="#fff").place(x=710,y=550)
root.mainloop()

