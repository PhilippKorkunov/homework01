import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext=""
    for i in range(len(plaintext)):
        s=plaintext[i]
        if ord(s)+shift > ord('z') and ord(s)>=ord('a') and ord(s)<=ord('z'):
            ciphertext+=chr(ord('a')+ord(s)+shift-ord('z')-1)
        elif ord(s)+shift > ord('Z') and ord(s)>=ord('A') and ord(s)<=ord('Z'):
            ciphertext+=chr(ord('A')+ord(s)+shift-ord('Z')-1)
        elif (ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z')):
            ciphertext+=chr(ord(s)+shift)
        else :
            ciphertext+=s
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        s=ciphertext[i]
        if ord(s)-shift <ord('a') and ord(s)>=ord('a') and ord(s)<=ord('z'):
            plaintext+=chr(ord('z')-(ord("a")-ord(s)+shift-1))
        elif ord(s)-shift < ord('A') and ord(s)>=ord('A') and ord(s)<=ord('Z'):
            plaintext+=chr(ord('Z')-(ord("A")-ord(s)+shift-1))
        elif (ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z')):
            plaintext+=chr(ord(s)-shift)
        else :
            plaintext+=s       
    return plaintext