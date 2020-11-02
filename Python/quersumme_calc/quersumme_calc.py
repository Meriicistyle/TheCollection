# Tool by Meriicistyle the Great
# The Quersumme Calculator (Shows the sum of the digits in a number.)
# There is no existing bug I know and I tested everything myself.
# Feel free to like it and it's licensed under the MERIICISTYLE CORP. LICENSE

print("""
        Enter a number to get the sum of the digits.
    """)

while True:
    num = int(input("Your number: "))
    sumnum = sum(int(digits) for digits in str(num))
    print(sumnum)