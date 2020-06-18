import random
import sys
import math

while True:
    print("""        
        --> Welcome to the Fibonacci
            number tester. To get
            started simply enter a number
            and learn is it's a Fibonacci
            number.
        """)

    numbertocheck = int(input("Number: "))

    squareroot1 = 5*numbertocheck*numbertocheck + 4
    squareroot2 = 5*numbertocheck*numbertocheck - 4

    result1 = math.sqrt(squareroot1)
    result2 = math.sqrt(squareroot2)

    if ((result1 == int) | (result2 == int)):
        print("""
        Your number is a Fibonacci number!
        ----------------------------------""")
        continue
    else:
        print("""
        Your number is no Fibonacci number.
        -----------------------------------""")
        continue