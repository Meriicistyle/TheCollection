import random

print("""
         To print a random numbers square
         between 12 and 100 just restart
         this script everytime.
         """)

for x in range(1):
    num = random.randint(12, 100)
    print(num * num)
