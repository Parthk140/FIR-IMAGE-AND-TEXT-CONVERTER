
from PIL import Image

import pytesseract as pt 
pt.pytesseract.tesseract_cmd= r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import os
import smtplib, ssl
import rt

import subprocess
import tkinter as tk

from tkinter import filedialog




root=tk.Tk

path =filedialog.askopenfilename()

    

def main(): 
    #name=input("enter name of file")
  
    
    fullTempPath ="D://Tess4J//tessdata//r.html"
         
        
    try:
        img  = Image.open(path)  
    except IOError:
        pass
  
        
         
    text = pt.image_to_string(img, lang ="eng") 

       
    file1 = open(fullTempPath, "a+") 
  
        
    file1.write(text+"\n")
      #  f=text+j
    file1.close()  

   
    file2 = open(fullTempPath, 'r') 
    print(file2.read()) 
    file2.close()
 
    search_word="sister"
    if search_word in text:
        with open(fullTempPath, mode='w', encoding='utf-8') as f2:
            text=text.replace(search_word, '<span style="color: red">{}</span>'.format(search_word))
            text=text.replace("\n","<br>")
            f2.write(text)
    else:
        print("The word is not in the text")
    f2.close()
    
    m1=rt.Mail()
    m1.main_account_screen()



 
    
 

  
    
if __name__ == '__main__': 
    main()
 