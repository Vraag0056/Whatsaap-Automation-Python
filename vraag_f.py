from tkinter import *
import os
from threading import Thread

def run_ex():
    Thread(target=run_ex_t1).start()

def run_ex_t1():
    os.system('py v-raag.py')

def run_sch():
    Thread(target=run_sch_t1).start()

def run_sch_t1():
    os.system('py schedule_m.py')

def run_send():
    Thread(target=run_send_t1).start()

def run_send_t1():
    os.system('py vraag_bulk_message_sender.py')

root = Tk()

root.title('Choose Option----Vraag')
root.geometry('340x330')
root.configure(bg="#fff")
root.resizable(False,False)



frame = Frame(root,width=350,height=480,bg="white")
frame.place(x=480,y=70)
heading = Label(root,text='Vraag', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=80,y=5)


Button(root,width=39,pady=7,text = 'Extract Number',bg='#57a1f8',fg='white',border=0,command=run_ex).place(x=30,y=80)
Button(root,width=39,pady=7,text = 'Send Message',bg='#57a1f8',fg='white',border=0,command=run_send).place(x=30,y=140)
Button(root,width=39,pady=7,text = 'Schedule Message',bg='#57a1f8',fg='white',border=0,command=run_sch).place(x=30,y=200)


root.mainloop()

