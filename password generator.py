from random import randint

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

length = 8

password = ""

for num in range(length):
    password += ALPHABET[randint(0,25)]
    
print(password)
