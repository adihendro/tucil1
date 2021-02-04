# GUI

from vigenere import *
from fullvigenere import *
from playfair import *

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

def compute():
    # Check if key empty
    if(ent_key.get()==''):
        messagebox.showerror('Error', 'Enter key!')
        return

    # Get text and key
    if(file_content == ''):
        text = ent_text.get().upper()
    else:
        text = file_content
    key = ent_key.get().upper()
    # Get mode
    mode = var1.get()
    # Get encryption type
    encType = var2.get()
    space = var3.get()
    if (space == '2'):
        if(encType=='1'): # Standard Vigenere Cipher
            lbl_result_text['text'] = addspace(mainVigenere(mode,text,key))
        elif(encType=='2'): # Full Vigenere Cipher
            lbl_result_text['text'] = addspace(fullVigenere(mode,text,key))
        elif(encType=='3'): # Auto-key Vigenere Cipher
            lbl_result_text['text'] = addspace(autoVigenere(mode,text,key))
        elif(encType=='4'): # Extended Vigenere Cipher
            lbl_result_text['text'] = extVigenere(mode,text,key)
        elif(encType=='5'): # Playfair Cipher
            lbl_result_text['text'] = addspace(playfairVigenere(mode,text,key))
    elif (space == '1'):
        if(encType=='1'): # Standard Vigenere Cipher
            lbl_result_text['text'] = mainVigenere(mode,text,key)
        elif(encType=='2'): # Full Vigenere Cipher
            lbl_result_text['text'] = fullVigenere(mode,text,key)
        elif(encType=='3'): # Auto-key Vigenere Cipher
            lbl_result_text['text'] = autoVigenere(mode,text,key)
        elif(encType=='4'): # Extended Vigenere Cipher
            lbl_result_text['text'] = extVigenere(mode,text,key)
        elif(encType=='5'): # Playfair Cipher
            lbl_result_text['text'] = playfairVigenere(mode,text,key)
    content = ''

file_content = ''

def openFile(): 
    f = askopenfile(mode ='rb') 
    if f is not None: 
        file_content = f.read() 

def addspace(a):
    return ' '.join([a[i:i + 5] for i in range(0, len(a), 5)])

# Clear function
def clear():
    ent_text.delete(0,END)
    ent_key.delete(0,END)

# Copy function
def copy():
    window.clipboard_clear()
    window.clipboard_append(lbl_result_text["text"])

# Exit function 
def qExit(): 
    window.destroy() 


# Main window
window = Tk()
window.title('Encrypt & Decrypt')

# Title label
lbl_title = Label(text='Welcome to Enigma!')
lbl_title.pack()

frm_form = Frame(relief=RIDGE, borderwidth=3)
frm_form.pack()

# Message label
lbl_text = Label(master=frm_form, text='Enter message:')
ent_text = Entry(master=frm_form, width=30)
lbl_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_text.grid(row=0, column=1, padx=5, pady=5)

# Key label
lbl_key = Label(master=frm_form, text='Enter key:')
ent_key = Entry(master=frm_form, width=30)
lbl_key.grid(row=1, column=0, padx=5, pady=5, sticky='w')
ent_key.grid(row=1, column=1, padx=5, pady=5)

btn_open = Button(master=frm_form, text='Open file', width=8, command=openFile)
btn_open.grid(row=2, column=1, padx=5, pady=5, sticky='w')
btn_clear = Button(master=frm_form, text='Clear', width=5, command=clear)
btn_clear.grid(row=2, column=1, padx=5, pady=5)

# Initialize radio button
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var1.set(1)
var2.set(1)
var3.set(1)

# Encryption mode
lbl_mode = Label(master=frm_form, text='Choose mode:')
lbl_mode.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rad_mode = Radiobutton(master=frm_form,text='Encryption', variable = var1, value=1)
rad_mode.grid(row=3, column=1, padx=5, pady=5, sticky='w')
rad_mode = Radiobutton(master=frm_form,text='Decryption', variable = var1, value=2)
rad_mode.grid(row=4, column=1, padx=5, pady=5, sticky='w')

# Encryption type
lbl_type = Label(master=frm_form, text='Choose type:')
lbl_type.grid(row=5, column=0, padx=5, pady=5, sticky="w")
rad_type = Radiobutton(master=frm_form,text='Vigenere Cipher', variable = var2, value=1)
rad_type.grid(row=5, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Full Vigenere Cipher', variable = var2, value=2)
rad_type.grid(row=6, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Auto-key Vigenere Cipher', variable = var2, value=3)
rad_type.grid(row=7, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Extended Vigenere Cipher', variable = var2, value=4)
rad_type.grid(row=8, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Playfair Cipher', variable = var2, value=5)
rad_type.grid(row=9, column=1, padx=5, pady=5, sticky='w')

# Print option
lbl_option = Label(master=frm_form, text='Choose print option:')
lbl_option.grid(row=10, column=0, padx=5, pady=5, sticky="w")
rad_option = Radiobutton(master=frm_form,text='Without space', variable = var3, value=1)
rad_option.grid(row=10, column=1, padx=5, pady=5, sticky='w')
rad_option = Radiobutton(master=frm_form,text='Separated every 5 letters', variable = var3, value=2)
rad_option.grid(row=11, column=1, padx=5, pady=5, sticky='w')

btn_compute = Button(master=frm_form, text='Go!', width=10, height=2, command=compute)
btn_compute.grid(row=13, column=1, padx=5, pady=5, sticky='w')

# Result label
lbl_result = Label(master=frm_form, text='Result:')
lbl_result_text = Label(master=frm_form, text='Click "Go!" to see magic')
lbl_result.grid(row=14, column=0, padx=5, pady=5, sticky="w")
lbl_result_text.grid(row=14, column=1, padx=5, pady=5, sticky="w")

btn_copy = Button(master=frm_form, text='Copy result', width=10, command=copy)
btn_copy.grid(row=15, column=1, padx=5, pady=5, sticky='w')
btn_exit = Button(master=frm_form, text='Exit', width=5, command=qExit)
btn_exit.grid(row=15, column=1, padx=5, pady=5, sticky='e')

# Keeps window alive 
window.mainloop()