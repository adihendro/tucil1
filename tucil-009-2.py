# Full Vigenere Cipher

import string
import random

# Import uppercase letters
LETTERS = string.ascii_uppercase
ORDINAL_A = ord('A')

def createMatrix():
    matrix = [0 for _ in range(26)]
    for i in range(26):
        matrix[i] = random.sample(LETTERS,26)
    return matrix

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
        cipher.append(matrix[ord(key[i]) - ORDINAL_A][ord(text[i]) - ORDINAL_A])
    return ''.join(cipher)

def decVigenere(cipher, key):
    text = []
    for i in range (len(cipher)):
        row = ord(key[i]) - ORDINAL_A
        n = matrix[row].index(cipher[i])
        text.append(LETTERS[n])
    return ''.join(text)

def main():
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


matrix = createMatrix()
# print(matrix)
main()