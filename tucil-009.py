# Vigenere Cipher

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


# Input text
text = input().upper() 
# Input key
key = input().upper()

clearedText = clearText(text)
clearedKey = clearText(key)

# print(clearedText)
print(extendKey(clearedText, clearedKey))

cipher = encVigenere(clearedText, extendKey(clearedText, clearedKey))
print(cipher)
print(decVigenere(cipher, extendKey(clearedText, clearedKey)))



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

def openFile(file):
    with open(file, 'rb') as f:
        return f.read()

def writeFile(text, filename):
    with open(filename, 'wb') as f:
        f.write(text)

# Open file in read only and binary mode
file = input()
text = openFile(file)
# Input key
key = input()

cipher = encExtendedVigenere(text, extendKey(text, key))
writeFile(bytearray(cipher), 'ciphered.txt')

cipher = openFile('ciphered.txt')
text = decExtendedVigenere(cipher, extendKey(text, key))
writeFile(bytearray(text), 'finished.docx')
'''