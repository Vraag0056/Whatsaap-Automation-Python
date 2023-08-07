from selenium.webdriver.support.wait import WebDriverWait
try:
    import Tkinter as tk
except:
    import tkinter as tk
from threading import Thread
from tkinter import filedialog as fd
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Vraag Bulk Message Sender")
        self.wm_iconbitmap("icon.ico")
        self.geometry('630x580')
        self.configure(bg="#fff")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

        self._frame.pack()


class StartPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#fff")
        tk.Label(self, text="Send Whatsaap Messages without saving number",bg='white',fg='#57a1f8', font=('Helvetica', 18, "bold"),pady=20).pack(side="top", fill="x",pady=40)
        tk.Button(self,width=25, text="Send by csv file",bg='#57a1f8',fg='white',border=0,
                  command=lambda: master.switch_frame(CsvFile),pady=10).pack(pady=20)
        tk.Button(self,width=25, text="Send by number only",bg='#57a1f8',fg='white',border=0,
                  command=lambda: master.switch_frame(SendIndividuals),pady=10).pack(pady=20)


    def attachments(self):
        attach = fd.askopenfilename()
        attach.append(attach)
        l4 = tk.Label(self, text=attach, font=('Helvetica', 12, "bold"))
        self.l4.pack()

class CsvFile(tk.Frame):
    name = []
    message=tk.Text
    attach=[]
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='white')
        tk.Button(self, text="Home", pady=10, padx=10, command=SampleApp, bg='#57a1f8', fg='white', border=0).pack(
            pady=10)
        tk.Label(self, text="Send by csv file", font=('Helvetica', 18, "bold"),pady=10,bg='white',fg='#57a1f8').pack(side="top", fill="x")
        tk.Label(self, text="Open your csv file", font=('Helvetica', 10, "bold"),pady=10,bg='white',fg='#57a1f8').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Choose CSV file",pady=10,command=self.callback,bg='#57a1f8',fg='white',border=0).pack(pady=10)
        self.l2 = tk.Label(self, text='', font=('Helvetica', 12, "bold"))
        self.message = tk.Text(self,height=10,border=5,bg = "#a6a1cc",)
        self.message.pack()
        tk.Button(self, text="Attachment", pady=10, padx=10, command=self.attachments,bg='#57a1f8',fg='white',border=0).pack(pady=10)
        self.l3 = tk.Label(self, text='', font=('Helvetica', 12, "bold"))
        self.l4 = tk.Label(self, text='', font=('Helvetica', 12, "bold"))
        tk.Button(self, text="Send", pady=10,padx=10,bg='#57a1f8',fg='white',border=0,
              command=self.threading).pack(pady=10)
        try:
            self.driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
            self.driver.get("https://web.whatsapp.com/")
        except:
            pass
        self.l3 = tk.Label(self, text='', font=('Helvetica', 12, "bold"))

    def threading(self):
        t1 = Thread(target=self.group_contact)
        t1.start()

    def save_unsavedContact(self,unsaved_contact, length, i,target_text,message):
        if len(self.attach) > 0 or len(message) > 0:
            try:
                link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(unsaved_contact)
                # driver  = webdriver.Chrome()
                self.driver.get(link)
                self.l3.destroy()
                self.l3 = tk.Label(self, text=target_text+":  "+str(i + 1) + "/" + str(length), font=('Helvetica', 12, "bold"))
                self.l3.pack()
                try:
                    time.sleep(5)
                    self.driver.implicitly_wait(10)
                    if len(self.attach) >0:
                        for x in self.attach:
                            time.sleep(2)
                            attachment_box = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH,'//div[@title = "Attach"]')))
                            attachment_box.click()
                            image_box = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH,
                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                            image_box.send_keys(x)
                            time.sleep(3)
                            send_button = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
                            send_button.click()
                            time.sleep(2)
                    if len(message) > 0:
                        input_box = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
                        """for ch in message:
                            if ch == "\n":
                                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
                                    Keys.ENTER).key_up(
                                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                            else:
                                input_box.send_keys(ch)
                        input_box.send_keys(Keys.ENTER)"""
                        input_box.send_keys(Keys.CONTROL + "v")
                        time.sleep(2)
                        input_box.send_keys(Keys.ENTER)
                        time.sleep(10)

                except Exception as e:
                     pass
                time.sleep(3)
            except:
                pass

    def group_contact(self):
        self.clipboard_append(self.message.get("1.0", "end-1c"))
        for j in range(0,len(self.name)):
            target_text=self.name[j]
            time.sleep(5)
            df = pd.read_csv(target_text)
            length = len(df.axes[0])

            for i in range(0, length):
                rf = df.loc[i, 'Phone 1 - Value']
                self.save_unsavedContact(rf, length, i,target_text,self.message.get("1.0", "end-1c"))

    def callback(self):
        wa = fd.askopenfilename()
        self.name.append(wa)
        self.l2 = tk.Label(self, text="CSV File: "+wa, font=('Helvetica', 12, "bold"))
        self.l2.pack()

    def attachments(self):
        attach = fd.askopenfilename()
        self.attach.append(attach)
        self.l4 = tk.Label(self, text="Attachment is: "+attach, font=('Helvetica', 12, "bold"))
        self.l4.pack()
class SendIndividuals(tk.Frame):
    message= tk.Text
    name= tk.Text
    attach=[]

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='white')
        tk.Button(self, text="Home", pady=10, padx=10, command=SampleApp, bg='#57a1f8', fg='white', border=0).pack(
            pady=10)
        tk.Label(self, text="Send by number", font=('Helvetica', 18, "bold"),bg='white',border=0,fg='#57a1f8').pack(side="top", fill="x", pady=5)
        tk.Label(self, text="Enter the number/numbers(seperated hy coma(,)) and starts with pin code(+91))",bg='white',border=0,fg='#57a1f8', font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=10)
        self.name = tk.Text(self,height=5,border=5)
        self.name.pack()
        tk.Label(self, text="Write your Message", font=('Helvetica', 12, "bold"),bg='white',border=0,fg='#57a1f8').pack(side="top", fill="x", pady=5)
        self.message = tk.Text(self,height=10,border=5)
        self.message.pack(pady=10)
        tk.Button(self, text="Attachment", pady=10, padx=10, command=self.attachments,bg='#57a1f8',fg='white',border=0).pack(pady=10)
        self.l3 = tk.Label(self, text='', font=('Helvetica', 12, "bold"))
        tk.Button(self, text="Send", pady=10, padx=10,command=self.threading,bg='#57a1f8',fg='white',border=0).pack(pady=10)
        self.l2=tk.Label(self, text='', font=('Helvetica', 12, "bold"),border=0,fg='#57a1f8')
        try:
            self.driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
            self.driver.get("https://web.whatsapp.com/")
        except:
            pass

    def threading(self):
        t1 = Thread(target=self.group_contact)
        t1.start()

    def save_unsavedContact(self,unsaved_contact, length, i,message):
        if len(self.attach) > 0 or len(message) > 0:
            try:
                link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(unsaved_contact)
                # driver  = webdriver.Chrome()
                WebDriverWait(self.driver, 200)
                time.sleep(5)
                self.driver.get(link)
                self.l3.destroy()
                self.l3 = tk.Label(self, text=str(i + 1) + "/" + str(length), font=('Helvetica', 12, "bold"))
                self.l3.pack()
                try:
                    time.sleep(2)
                    self.driver.implicitly_wait(10)
                    if len(self.attach) > 0:
                        for x in self.attach:
                            time.sleep(2)
                            attachment_box = WebDriverWait(self.driver, 300).until(
                                EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]')))
                            attachment_box.click()
                            image_box = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH,
                                                                                                              '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                            image_box.send_keys(x)
                            time.sleep(3)
                            send_button = WebDriverWait(self.driver, 300).until(
                                EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
                            send_button.click()
                            time.sleep(10)

                    if len(message) > 0:
                        input_box = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
                        """for ch in message:
                            if ch == "\n":
                                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
                                    Keys.ENTER).key_up(
                                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                            else:
                                input_box.send_keys(ch)"""
                        input_box.send_keys(Keys.CONTROL+"v")
                        time.sleep(2)
                        input_box.send_keys(Keys.ENTER)
                        time.sleep(10)
                except Exception as e:
                    pass
                time.sleep(3)
            except:
                pass

    def group_contact(self):
        wa = self.name.get("1.0", "end-1c")
        target_text=list(wa.split(","))

        length = len(target_text)
        self.clipboard_append(self.message.get("1.0", "end-1c"))
        for i in range(0, length):
            self.save_unsavedContact(target_text[i], length, i,self.message.get("1.0", "end-1c"))

    def attachments(self):
        attach = fd.askopenfilename()
        self.attach.append(attach)
        self.l2 = tk.Label(self, text="Attachment is: "+attach, font=('Helvetica', 12, "bold"))
        self.l2.pack()

if __name__ == "__main__":
    try:
        app = SampleApp()
        app.mainloop()
    except:
        pass

