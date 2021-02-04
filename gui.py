# GUI

from tkinter import *
from tkinter.filedialog import askopenfile

def increase():
    value = lbl_result_text['text']
    lbl_result_text['text'] = 'changed'

def openFile(): 
    file = askopenfile(mode ='rb') 
    if file is not None: 
        content = file.read() 
        print(content)


window = Tk()
window.title('Encrypt & Decrypt')

lbl_title = Label(text='Welcome to Enigma!')
lbl_title.pack()

frm_form = Frame(relief=RIDGE, borderwidth=3)
frm_form.pack()

lbl_plaintext = Label(master=frm_form, text='Enter message:')
ent_plaintext = Entry(master=frm_form, width=40)
lbl_plaintext.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_plaintext.grid(row=0, column=1, padx=5, pady=5)

lbl_key = Label(master=frm_form, text='Enter key:')
ent_key = Entry(master=frm_form, width=40)
lbl_key.grid(row=1, column=0, padx=5, pady=5, sticky='w')
ent_key.grid(row=1, column=1, padx=5, pady=5)

btn_open = Button(master=frm_form, text='Open file', width=10, command=openFile)
btn_open.grid(row=2, column=1, padx=5, pady=5, sticky='w')

var1 = StringVar()
var2 = StringVar()
var1.set(0)
var2.set(0)

lbl_type = Label(master=frm_form, text='Choose encryption:')
lbl_type.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rad_type = Radiobutton(master=frm_form,text='Vigenere Cipher', variable = var1, value=1)
rad_type.grid(row=3, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Full Vigenere Cipher', variable = var1, value=2)
rad_type.grid(row=4, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Auto-key Vigenere Cipher', variable = var1, value=3)
rad_type.grid(row=5, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Extended Vigenere Cipher', variable = var1, value=4)
rad_type.grid(row=6, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Playfair Cipher', variable = var1, value=5)
rad_type.grid(row=7, column=1, padx=5, pady=5, sticky='w')

lbl_type = Label(master=frm_form, text='Choose text option:')
lbl_type.grid(row=8, column=0, padx=5, pady=5, sticky="w")
rad_type = Radiobutton(master=frm_form,text='Without space', variable = var2, value=1)
rad_type.grid(row=8, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Separated every 5 letters', variable = var2, value=2)
rad_type.grid(row=9, column=1, padx=5, pady=5, sticky='w')

btn_compute = Button(master=frm_form, text='Go!', width=10, command=increase)
btn_compute.grid(row=10, column=1, padx=5, pady=5, sticky='w')

lbl_result = Label(master=frm_form, text='Result:')
lbl_result_text = Label(master=frm_form, text='R')
lbl_result.grid(row=11, column=0, padx=5, pady=5, sticky="w")
lbl_result_text.grid(row=11, column=1, padx=5, pady=5, sticky="w")


# Keeps window alive 
window.mainloop()