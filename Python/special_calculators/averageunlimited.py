# Tool by Meriicistyle the Great
# The Unlimited Average Calculator
# Written in Pure Python.
# There is no existing bug I know and I tested everything myself.

# The tour and average section where we define the loop and the average at the beginning.
tour = 0
average = 0

# That's where we print the 'Welcome to our Tool Message and we explain them how the tool works.
print("""        
        Welcome to the average calculator.
        Enter your number and press Enter,
        your numbers will be added to a list.
        Press 'q' to get the average.
        """)

# Here we start the loop and that's as you know the place where it 'replays' everything.
while True:

    # We defined our list format and the limit for the length of the list.
    list = []
    maxLengthList = 99999999999999999

    # Here we start a loop inside a LOOP
    while len(list) < maxLengthList:
        num = input("Sayı giriniz: ")
        if num == "q":
            print(sum(list) / float(len(list)))
            break
        list.append(int(num))
        tour += 1

        print(list)