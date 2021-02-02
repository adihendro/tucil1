
from tkinter import *
import random 
import string
import itertools
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
  
# Function to encode 
alphabets = "abcdefghijklmnopqrstuvwxyz"
# Vigenere Cipher Standard (26 huruf alfabet)

def encode1(key, text):
    enc = ""
    keyindex = []
    for x in key:
        keyindex.append(alphabets.find(x))

    i = 0
    for x in text:
        if i == len(keyindex):  
            i = 0
        if x != ' ':
            pos = alphabets.find(x) + keyindex[i]
            print(pos)
            if pos > 25:
                pos = pos-26
            enc += alphabets[pos].capitalize()
            i +=1
        else:
            continue
    return enc


# Full Vigenere Cipher


# Auto-Key Vigenere
def encode3(key, text):
    
    keyindex = []
    for x in key:
        keyindex.append(alphabets.find(x))
        for y in text:
            if y != ' ':
                keyindex.append(alphabets.find(y))
            else:
                continue
    enc =""
    i = 0
    for x in text:
        if x != ' ':
            pos = alphabets.find(x) + keyindex[i]
            print(pos)
            if pos > 25:
                pos = pos-26
            enc += alphabets[pos].capitalize()
            i +=1
        else:
            continue
    return enc
    

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

def bigram(text):           # membuat plaintext jadi bigram/pasangan huruf
    t = []
    for i in text:
        t.append(i)
    
    for i in range(len(t)): # mengeliminasi spasi
        if " " in t:
            t.remove(" ")
    
    j = 0
    for i in range(len(t)//2):   # kalau ada huruf yang sama
        if t[i] == t[i+1]:
            t.insert(i+1,'x')
        i = i+2
    
    if len(t)%2 == 1:   # kalau jumlah huruf di plaintext ganjil
        t.append("x")
    
    j = 0
    newtext = []
    for x in range(1, len(t)//2+1):
        newtext.append(t[j:j+2])
        j = j+2
    return newtext

def cleaninput(text):
    text = ''.join([c.upper() for c in text if c in string.ascii_letters]) # membuat karakter menjadi kapital
    clean = ""

    if len(text) < 2:
        return text
    for i in range(len(text)-1):
        clean += text[i]
        if text[i] == text[i+1]:        # jika ada karakter yang sama
            clean += 'X'
    clean += text[-1]

    if len(clean) & 1:      # jika jumlah karakter text ganjil
        clean += 'X'
    return clean

def generate_key(key):
    withoutj = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []

    for i in key.upper():   
        if i not in table and i in withoutj:    # masukin karakter selain j dari key
            table.append(i)
    for i in withoutj:
        if i not in table:           # masukin karakter yang tersisa
            table.append(i)
    
    return table


def encode5(key,text):
    table = generate_key(key)
    plaintext = cleaninput(text)
    enc = ""

    for a,b in bigram(plaintext):
        row1,col1 = divmod(table.index(a), 5)
        row2,col2 = divmod(table.index(b), 5)

        if row1 == row2:                        # kalau berada di baris yang sama
            enc += table[row1*5+(col1+1)%5]
            enc += table[row2*5+(col2+1)%5]
        elif col1 == col2:                         # kalau berada di kolom yang sama
            enc += table[(col1+((row1+1)%5)*5)]
            enc += table[(col2+((row2+1)%5)*5)]
        else:
            enc += table[row1*5+col2]
            enc += table[row2*5+col1]
    return enc
 

  
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
  
  
def Ref(): 
    print("Message = ", (Msg.get())) 
  
    text = Msg.get() 
    k = key.get() 
    m = mode.get() 
    c = cip.get()
  
    if (m == 'e'): #encode
        if (c == 'a'):
            Result.set(encode1(k,text))
        if (c == 'c'):
            Result.set(encode3(k,text))
        if (c == 'd'):
            Result.set(encode4(k, text)) 
        if (c == 'e'):
            Result.set(encode5(k,text))
        #else:
    


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
                  command = lambda : save()).grid(row = 7, column = 4) 
  
# keeps window alive 
root.mainloop() 