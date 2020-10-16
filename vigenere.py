def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext=""
    n=len(plaintext)//len(keyword)+1
    keyword*=n
    for i in range(len(plaintext)):
        if ord(keyword[i])>=ord('a') and ord(keyword[i])<=ord('z'):
            shift=ord(keyword[i])-ord('a')
        if ord(keyword[i])>=ord('A') and ord(keyword[i])<=ord('Z'):
            shift=ord(keyword[i])-ord('A')    
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


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    n=len(ciphertext)//len(keyword)+1
    keyword*=n   
    for i in range(len(ciphertext)):
        if ord(keyword[i])>=ord('a') and ord(keyword[i])<=ord('z'):
            shift=ord(keyword[i])-ord('a')
        if ord(keyword[i])>=ord('A') and ord(keyword[i])<=ord('Z'):
            shift=ord(keyword[i])-ord('A')
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