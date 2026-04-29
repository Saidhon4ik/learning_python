import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"keys: {key}")     <---- it is in the comments not to show our chars and keys, if u want you can even create a file to store them in, but not yet, it is 
#too early for now


#encrypting
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")



#decryption
cipther_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipther_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original: {plain_text}")
