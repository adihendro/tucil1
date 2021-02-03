# Vigenere Cipher

def clearText(text):
    clearedText = []
    for i in range (len(text)):
        if (text[i].isalpha()):
            clearedText.append(text[i])
    return "".join(clearedText)

def extendKey(text, key):
    key = list(key)
    for i in range (len(text)-len(key)):
        key.append(key[i%len(key)])
    return "".join(key)

def encVigenere(text, key):
    cipher = []
    for i in range (len(text)):
        cipher.append(chr((ord(text[i]) + ord(key[i]))%26 + ord("A")))
    return "".join(cipher)

def decVigenere(cipher, key):
    text = []
    for i in range (len(cipher)):
        text.append(chr((ord(cipher[i]) - ord(key[i]))%26 + ord("A")))
    return "".join(text)

# Input text
text = input().upper() 
# Input key
key = input().upper()

clearedText = clearText(text)
clearedKey = clearText(key)
print(clearedText)
print(extendKey(clearedText, clearedKey))

cipher = encVigenere(clearedText, extendKey(clearedText, clearedKey))
print(cipher)
print(decVigenere(cipher, extendKey(clearedText, clearedKey)))
