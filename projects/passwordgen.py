# Password Generator
# 5/6/2023

import random
import string

def pass_gen(l):
    digits = input("Include digits? (Y/N) ")
    punc = input("Include punctuation? (Y/N) ")
    if digits == 'N' and punc == 'N':
        characters = string.ascii_letters
    elif digits == 'Y' and punc == 'N':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(l))
    return password

password = pass_gen(int(input("Enter the length of your password: ")))
print(password)