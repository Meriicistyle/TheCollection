import sys
import random
import math

while True:
    print("""        
        --> Welcome to the Fibonacci
            number tester. Simply
            enter your number to learn
            if it is a Fibonacci number.
        """)
    fibo = int(input("Number: "))
    fibostring = str(fibo)
    fiboup = 5*fibo*fibo+4
    fibodown = 5*fibo*fibo-4

    def isPerfectSquare(x): 
        sr = math.sqrt(x)  
        return ((sr - math.floor(sr)) == 0)

    if (isPerfectSquare(fiboup)) or (isPerfectSquare(fibodown)):
        print("")
        print(fibostring + """ IS a Fibonacci number.
-----------------------------""")
        continue
    else:
        print("")
        print(fibostring + """ is NOT a Fibonacci number.
-----------------------------""")
        continue