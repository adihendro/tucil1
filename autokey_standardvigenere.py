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