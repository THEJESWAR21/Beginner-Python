import random
import secrets
import string

digits = string.digits
punctuation = string.punctuation
ascii_letters = string.ascii_letters

selection_list = digits + punctuation + ascii_letters

password_len = int(input("Input Password Length: "))


while True:
    password = ''
    for i in range(password_len):
        password +=''.join(secrets.choice(selection_list))
        i = i + 1
    # CUSTOMIZING THE GENERATED CODE
    # if any(char in ascii_letters for char in password) and sum(char in digits for char in password) == 2 and i == password_len:
    #     print(password)
    #     break
    if i == password_len:
        print(password)
        break
    
        


# Customizing The Generated Code
