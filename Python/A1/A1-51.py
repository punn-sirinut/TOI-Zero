def caesar_cipher_encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char      
    return result
message = input()
shift = int(input())
print(caesar_cipher_encrypt(message, shift))