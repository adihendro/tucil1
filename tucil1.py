
from tkinter import *
import random 
import string
import itertools
import tkinter

# import cipher
from playfair import encPlayfair, decPlayfair
from vigenere import *
from tkinter.filedialog import asksaveasfile 
  
# creating root object 
root = Tk() 
  
# defining size of window 
root.geometry("1200x900") 
  
# setting up the title of window 
root.title("Tucil 1 - Encryption and Decryption") 
  
Tops = Frame(root, width = 1000, relief = SUNKEN) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 100, height = 100, 
                            relief = SUNKEN) 
f1.pack(side = LEFT) 
  
cip = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
  
# exit function 
def qExit(): 
    root.destroy() 

def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
  
# Function to reset the window 
def Reset(): 
    cip.set("") 
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 
  
  
lblReference = Label(f1, font = ('calibri', 16, 'bold'), 
                text = "Cipher Type\n" "a. Vigenere Cipher Standard\n"
                "b. Full Vigenere Cipher\n"
                "c. Auto Key Vigenere Cipher\n"
                "d. Extended Vigenere Cipher\n"
                "e. Playfair Cipher", bd = 15, anchor = "center") 
                  
lblReference.grid(row = 0, column = 0) 
  
txtReference = Entry(f1, font = ('calibri', 16, 'bold'), 
               textvariable = cip, bd = 10, insertwidth = 4, 
                        bg = "powder blue", justify = 'right') 
                          
txtReference.grid(row = 0, column = 1) 
  
lblMsg = Label(f1, font = ('calibri', 16, 'bold'), 
         text = "MESSAGE", bd = 65, anchor = "w") 
           
lblMsg.grid(row = 1, column = 0)
  
txtMsg = Entry(f1, font = ('calibri', 16, 'bold'), 
         textvariable = Msg, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtMsg.grid(row = 1, column = 1, sticky=N+E+S+W) 
  
lblkey = Label(f1, font = ('calibri', 16, 'bold'), 
            text = "KEY", bd = 16, anchor = "w") 
              
lblkey.grid(row = 2, column = 0) 
  
txtkey = Entry(f1, font = ('calibri', 16, 'bold'), 
         textvariable = key, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtkey.grid(row = 2, column = 1) 
  
lblmode = Label(f1, font = ('calibri', 16, 'bold'), 
          text = "MODE\n""(e for encrypt, d for decrypt)", 
                                bd = 16, anchor = "w") 
                                  
lblmode.grid(row = 3, column = 0) 
  
txtmode = Entry(f1, font = ('calibri', 16, 'bold'), 
          textvariable = mode, bd = 10, insertwidth = 4, 
                  bg = "powder blue", justify = 'right') 
                    
txtmode.grid(row = 3, column = 1) 
  
lblService = Label(f1, font = ('calibri', 16, 'bold'), 
             text = "The Result =", bd = 16, anchor = "w") 
               
lblService.grid(row = 2, column = 2) 
  
txtService = Entry(f1, font = ('calibri', 16, 'bold'),  
             textvariable = Result, bd = 10, insertwidth = 4, 
                       bg = "powder blue", justify = 'right') 
                         
txtService.grid(row = 2, column = 3) 
  
# Vigenère cipher 
import base64 
  

# Extended Vigenere Cipher *** belum bener
def encode4(key, text): 
    enc = [] 
      
    for i in range(len(text)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(text[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 

# Playfair Cipher



  
# Function to decode 
def decode4(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  

def addspace(a):
    return ' '.join([a[i:i + 5] for i in range(0, len(a), 5)])

def Ref(): 
    print("Message = ", (Msg)) 
  
    text = Msg.get()
    k = key.get()
    m = mode.get() 
    c = cip.get()
    hasil = ''
  
    if (m == 'e'): #encode
        if (c == 'a'):
            #Result.set(addspace(encVigenere(text, (extendKey(clearText(text), clearText(key)))))) # standard vigenere
            hasil = encVigenere(clearText(text), extendKey(clearText(text), clearText(k)))
            Result.set(addspace(hasil))
        #if (c == 'b'):
            #Result.set(encode2(k,text)) # full key
        if (c == 'c'):
            Result.set(addspace(encVigenere(k,text))) # autokey vigenere
        if (c == 'd'):
            Result.set(addspace(encExtendedVigenere(text, extendKey(text, k)))) # extended vigenere
        if (c == 'e'):
            Result.set(addspace(encPlayfair(k,text))) # playfair
    
    elif (m == 'd'):
        if (c == 'a'):
            Result.set(addspace(decVigenere(text, (extendKey(clearText(text), clearText(k))))))
       # if (c == 'b'):
        
        #if (c == 'c'):

        if (c == 'd'):
            Result.set(addspace(decExtendedVigenere(text, (extendKey(text, k))))) 
        if (c == 'e'):
            Result.set(addspace(decPlayfair(k,text)))
        #else:
    
def write_File (text_File):
    file = open("resultsave.txt", "a")
    user_Input = text_File.get()
    file.write(user_Input)
    file.close()



# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Show Message", bg = "powder blue", 
                         command = Ref).grid(row = 7, column = 1) 
  
# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 7, column = 2) 
  
# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 7, column = 3) 

# Save button
btnSave = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Save", bg = "silver", 
                  command = lambda : write_File(Result)).grid(row = 7, column = 4) 
  
# keeps window alive 
root.mainloop() 