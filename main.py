from random import *
from datetime import datetime
from art import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

time = datetime.now()

tprint("Password Generator")
tprint(f"It's currently {time.strftime('%H:%M:%S')}", "minion")
print("+––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––+")

while True:
    len = int(input("How long should your password be: "))
    word = str(input("What should your password contain: "))

    passletters = word
    for i in range(len):
        passletters += alphabet[randrange(0, 23)]
        password = passletters

    print("\n\n\nYour new Password")
    tprint(password)

    if input("Happy? y or n: ") == "y":
        break