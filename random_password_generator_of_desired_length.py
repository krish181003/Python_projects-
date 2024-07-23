import string
import random

possible_values = string.ascii_letters+string.digits+string.punctuation

def my_password_desired_length(q):
    a = int(input("length of your password: "))  

    pass_len = a                                                    
    password = ""

    for x in range(pass_len):
        password += random.choice(possible_values)

    print("your random password:", password)

my_password_desired_length(possible_values)
 