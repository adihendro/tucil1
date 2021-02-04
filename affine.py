# Affine cipher

ORDINAL_A = ord('A')
N = 26
M = 7

def clearText(text):
    clearedText = []
    for i in range (len(text)):
        if (text[i].isalpha()):
            clearedText.append(text[i])
    return ''.join(clearedText)

def invers(M):
    Mi = i = 0
    while Mi != 1:
        i+=1
        Mi = (M * i) %N
    return i

def encAffine(text, b):
    cipher = []
    for i in range (len(text)):
        cipher.append(chr((M * (ord(text[i]) - ORDINAL_A) + b) %N + ORDINAL_A))
    return ''.join(cipher)

def decAffine(cipher, b):
    Mi = invers(M)
    text = []
    for i in range (len(cipher)):
        text.append(chr((Mi * (ord(cipher[i]) - ORDINAL_A - b)) %N + ORDINAL_A))
    return ''.join(text)


'''
# Input text
text = input().upper() 
# Input m key
m = int(input())
# Input b key
b = int(input())

clearedText = clearText(text)

cipher = encAffine(clearedText, m, b)
print(cipher)

print(decAffine(cipher, m, b))
'''