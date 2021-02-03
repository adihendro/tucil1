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

# Auto-Key Vigenere Cipher
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

def decode1(key,text):
    keyindex = []
    hasil = ""
    for x in key:
        keyindex.append(alphabets.find(x))
        i = 0
    for x in text:
        if i == len(keyindex):  
            i = 0
        if x != ' ':
            pos = alphabets.find(x.lower()) - keyindex[i]
            print(pos)
            if pos < 0:
                pos = pos+26
            hasil += alphabets[pos].lower()
            i +=1
        else:
            continue
    return hasil        

def decode3(key,text):
    keyindex = []
    hasil = ""
    for x in key:
        keyindex.append(alphabets.find(x))
        for y in text:
            if y != ' ':
                keyindex.append(alphabets.find(y))
            else:
                continue
        i = 0
    for x in text:
        if i == len(keyindex):  
            i = 0
        if x != ' ':
            pos = alphabets.find(x.lower()) - keyindex[i]
            print(pos)
            if pos < 0:
                pos = pos+26
            hasil += alphabets[pos].lower()
            i +=1
        else:
            continue
    return hasil        