import random
import sys

print("""        
        Welcome to the Number
        Guessing game. Enter a
        number and try to guess
        it based on given infor-
        mation! (Numbers between
        0 and 1000 allowed only.)
        """)

randomnum = int(random.randint(0, 1000))

while True:
    num = int(input("Number: "))

    if (num==randomnum):
        print("You found the number!")
        sys.exit()
    elif (num>randomnum):
        print("Lower! Try again.")
        continue
    elif (num<randomnum):
        print("Higher! Try again.")
        continue