# Standard Vigenere Cipher

ORDINAL_A = ord('A')

def clearText(text):
    clearedText = []
    for i in range (len(text)):
        if (text[i].isalpha()):
            clearedText.append(text[i])
    return ''.join(clearedText)

def extendKey(text, key):
    key = list(key)
    for i in range (len(text) - len(key)):
        key.append(key[i % len(key)])
    return ''.join(key)

def autoKey(text, key):
    key = list(key)
    for i in range (len(text) - len(key)):
        key.append(text[i % len(key)])
    return ''.join(key)

def encVigenere(text, key):
    cipher = []
    for i in range (len(text)):
        cipher.append(chr((ord(text[i]) + ord(key[i])) %26 + ORDINAL_A))
    return ''.join(cipher)

def decVigenere(cipher, key):
    text = []
    for i in range (len(cipher)):
        text.append(chr((ord(cipher[i]) - ord(key[i])) %26 + ORDINAL_A))
    return ''.join(text)

def mainVigenere(mode, text, key):
    clearedText = clearText(text)
    clearedKey = clearText(key)
    if(mode=='1'): # Encryption
        cipher = encVigenere(clearedText, extendKey(clearedText, clearedKey))
    else: # Decryption
        cipher = decVigenere(text, extendKey(clearedText, clearedKey))
    return cipher

def autoVigenere(mode,text,key):
    clearedText = clearText(text)
    clearedKey = clearText(key)
    if(mode=='1'): # Encryption
        cipher = encVigenere(clearedText, autoKey(clearedText, clearedKey))
    else: # Decryption
        cipher = decAutoVigenere(clearedText,key)
    return cipher

# Auto-Key Vigenere Cipher

def decAutoVigenere(cipher,key):
    text = []
    keyindex = []
    for x in key:
        keyindex.append(x)
    for i in range (len(cipher)):
        if (len(text)) != (len(keyindex)):
            text.append(chr((ord(cipher[i]) - ord(keyindex[i])) %26 + ORDINAL_A))
            keyindex.append(chr((ord(cipher[i]) - ord(keyindex[i])) %26 + ORDINAL_A))
    return ''.join(text)


'''
clearedText = clearText(text)

# print(clearedText)
print(autoKey(clearedText, key))

cipher = decAutoVigenere(clearText(text), key)

print(cipher)
#print(decVigenere(cipher, key))

'''

# Extended Vigenere Cipher

def encExtendedVigenere(text, key):
    cipher = []
    for i in range (len(text)):
        cipher.append((text[i] + ord(str(key[i]))) %256)
    return cipher

def decExtendedVigenere(cipher, key):
    text = []
    for i in range (len(cipher)):
        text.append((cipher[i] - ord(str(key[i]))) %256)
    return text

# Open file in read only and binary mode
def openFile(file):
    with open(file, 'rb') as f:
        return f.read()

# Write file in write and binary mode
def writeFile(text, filename):
    with open(filename, 'wb') as f:
        f.write(text)

def extVigenere(mode,text,key):
    clearedKey = clearText(key)
    if(mode=='1'): # Encryption
        cipher = encExtendedVigenere(text, extendKey(text, clearedKey))
        writeFile(bytearray(cipher), 'cipheredtext.txt')
    else: # Decryption
        cipher = decExtendedVigenere(text, extendKey(text, clearedKey))
        writeFile(bytearray(text), 'finished.txt')
    return cipher


'''
file = input()
text = openFile(file)

key = input().upper()
clearedKey = clearText(key)

cipher = encExtendedVigenere(text, extendKey(text, clearedKey))
writeFile(bytearray(cipher), 'ciphered.txt')

cipher = openFile('ciphered.txt')
text = decExtendedVigenere(cipher, extendKey(text, clearedKey))
writeFile(bytearray(text), 'finished.docx')
'''