# Affine cipher

ORDINAL_A = ord('A')
N = 26

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

def encAffine(text, m, b):
    cipher = []
    for i in range (len(text)):
        cipher.append(chr((m * (ord(text[i]) - ORDINAL_A) + b) %N + ORDINAL_A))
    return ''.join(cipher)

def decAffine(cipher, m, b):
    Mi = invers(m)
    text = []
    for i in range (len(cipher)):
        text.append(chr((Mi * (ord(cipher[i]) - ORDINAL_A - b)) %N + ORDINAL_A))
    return ''.join(text)


'''
# Input text
text = input().upper() 
# Input bm key
m = int(input())
# Input b key
b = int(input())

clearedText = clearText(text)

cipher = encAffine(clearedText, m, b)
print(cipher)

print(decAffine(cipher, m, b))
'''