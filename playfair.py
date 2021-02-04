import string
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


def encPlayfair(key,text):
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

def decPlayfair(key,text):
     table = generate_key(key)
     hasil = ""

     for a,b in bigram (text):
        row1, col1 = divmod(table.index(a), 5)
        row2, col2 = divmod(table.index(b), 5)

        if row1 == row2:
            hasil += table[row1*5+(col1-1)%5]
            hasil += table[row2*5+(col2-1)%5]
        elif col1 == col2:
            hasil += table[((row1-1)%5)*5+col1]
            hasil += table[((row2-1)%5)*5+col2]
        else:
            hasil += table[row1*5+col2]
            hasil += table[row2*5+col1]
     return hasil