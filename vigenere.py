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

def mainVigenere(text, key):
    clearedText = clearText(text)
    clearedKey = clearText(key)
    cipher = encVigenere(clearedText, extendKey(clearedText, clearedKey))
    cipher = decVigenere(cipher, extendKey(clearedText, clearedKey))
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
            keyindex.append(text[i])
    return ''.join(text)

   


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


def openFile(file):
    with open(file, 'rb') as f:
        return f.read()

def writeFile(text, filename):
    with open(filename, 'wb') as f:
        f.write(text)

# Open file in read only and binary mode
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