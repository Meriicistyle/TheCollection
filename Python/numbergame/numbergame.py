while True:
    number = int(input("Enter a number: "))

    if (number%2==0 and number%4==0):
        print("Your number is a multiple of 4.")
    elif (number%2==0 and number%4!=0):
        print("Your number is even.")
    else:
        print("Your number is an odd one.")