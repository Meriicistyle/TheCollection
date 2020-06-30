import string
import math
import secrets

while True:
    print("""
    Welcome to the password generator!
    Built by Meriicistyle this tool
    uses very 'basic' creating algo-
    rithms. Used pure Python random.""")

#Variables sequentially for the password length, uppercase letters, number choice, special characters and redotime.
    length = int(input("How long will your password be: "))
    uppercase = str.lower(input("Upper case letters? (Y)es or (N)o: "))
    lowercase = str.lower(input("Lower case letters? (Y)es or (N)o: "))
    numchoice = str.lower(input("Should numbers be included? (Y)es or (N)o: "))
    special = str.lower(input("Any special characters (e.g. %&+^^)? (Y)es or (N)o: "))
    redotime = int(secrets.randbelow(length))

    upperletters = string.ascii_lowercase
    lowletters = string.ascii_uppercase
    allletters = string.ascii_letters