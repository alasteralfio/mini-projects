# Caesar Cipher
# 7/6/2023

def caesar_encrypt(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            encrypted_char = chr((ord(char.lower()) - 97 - 3) % 26 + 97)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            decrypted_char = chr((ord(char.lower()) - 97 + 3) % 26 + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

choice = input("Encrypt or decrypt? (E/D) ")
message = input("Enter the message: ")
if choice == 'E':
    print(caesar_encrypt(message))
else:
    print(caesar_decrypt(message))