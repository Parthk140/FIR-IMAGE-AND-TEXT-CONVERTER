from tkinter import *


import smtplib, ssl

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


import os
fullTempPath ="D://Tess4J//tessdata//r.html" 
class Mail:
    def Mail(self):
        self.fullTempPath ="D://Tess4J//tessdata//r.html"


 
    def login(self):
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
     
        global username_verify
        global password_verify
        global name_verify
        username_verify = StringVar()
        name_verify = StringVar()
        password_verify = StringVar()
     
        global username_login_entry
        global password_login_entry
        global name_login_entry
        Label(login_screen, text="Sender MAIL ID * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="Reciever MAIL ID * ").pack()
        name_login_entry = Entry(login_screen,textvariable=name_verify)
        name_login_entry.pack()
        Label(login_screen, text="").pack()
        
        Button(login_screen, text="Login", width=10, height=1,command = self.mail ).pack()


        
    def mail(self):
        global username_verify
        global password_verify
        global name_verify
        fromaddr =username_login_entry.get()
        toaddr =  name_login_entry.get()
        password=password_login_entry.get()
        print(""+fromaddr)

        msg = MIMEMultipart() 
      

        msg['From'] = fromaddr 
      
     
        msg['To'] = toaddr 
      

        msg['Subject'] = "Subject of the Mail"
      
     
        body = "Body_of_the_mail"
      

        msg.attach(MIMEText(body, 'plain')) 
      
     
        filename = "r.html"
        attachment = open(fullTempPath, "rb") 
        

        p = MIMEBase('application', 'octet-stream') 
      

        p.set_payload((attachment).read()) 
      

        encoders.encode_base64(p) 
       
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      

        msg.attach(p) 
      

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()       
        s.login(fromaddr, password)       
        text = msg.as_string()            
        s.sendmail(fromaddr, toaddr, text)       
        s.quit()

        
        

     
    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Enter mailing detail")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()
        main_screen.mainloop()
 
 
#main_account_screen()