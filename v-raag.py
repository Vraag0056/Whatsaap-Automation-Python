import csv
from threading import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import time
import tkinter.messagebox
from selenium import webdriver

def threading():
    t1=Thread(target=printel)
    t1.start()



def group_contact(target_text):
        try:
            rb_results = []
            time.sleep(5)
            elm = WebDriverWait(driver, 70000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/header/div[2]/div[2]/span'))).text

            if elm == "click here for contact info" or elm==None:
                        rb_results.append("0")
                        print("end")

            else:
                    rb_results.append(elm)
                    print("go on...")

            with open ("group_contact/rb_results.csv","w", newline='') as resultFile:
                        print("process go on ")
                        writer = csv.DictWriter(resultFile, fieldnames=["Rb Results"],delimiter=',')
                        writer.writeheader()
                        writer.writerows({'Rb Results': item} for item in rb_results)
                        resultFile.close()
            df = pd.read_csv("group_contact/rb_results.csv")
            rf=df.loc[0, 'Rb Results']
            rf=rf.replace(",","\n")
            x= rf.split("\n")
            rf=''
            im = 1
            for el in x:
                if(el.startswith(' +')):
                    rf=rf + str(target_text)+str(im) +  ",* myContacts," + str(el)+ "\n"
                    im= im + 1
            f = open('group_contact/'+target_text+'.csv','w', encoding="utf-8")
            f.write("Name,Group Membership,Phone 1 - Value\n")
            f.write(rf)
            f.close()
            if rb_results!="0" or len(rb_results)!=0:
                tkinter.messagebox.showinfo("Success!!", "Number is saved in group contact file and the file ame is same as your search name")
        except:
            pass
def printel():
    target = e1.get()
    print("go on....")
    time.sleep(5)
    group_contact(target)
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\jaind\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)
window = Tk()

window.title('V-RAAG')
window.wm_iconbitmap('icon.ico')
window.resizable(0, 0)
l1 = Label(window, text="Save")
l1.grid(row=0, column=1)
target_text = StringVar()
e1 = Entry(window, textvariable=target_text)
e1.grid(row=0, column=2)
l2 = Label(window, text=" ")
l2.grid(row=1, column=2)
mybutton = Button(window, text="Enter",command=threading)
mybutton.grid(row=0, column=3, padx=10, pady=10)
window.mainloop()

