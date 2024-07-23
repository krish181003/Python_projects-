import string
import random

possible_values = string.ascii_letters+string.digits+string.punctuation

def my_password_select_range(t):
    t = int(input("starting range: "))
    y = int(input("ending range: "))

    b = random.randint(t, y) 

    pass_len = b                                                   
    password = ""

    for x in range(pass_len):
        password += random.choice(possible_values)

    print("your random password:", password)

my_password_select_range(possible_values)