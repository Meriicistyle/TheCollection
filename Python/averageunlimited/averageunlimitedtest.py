# Tool by Meriicistyle the Great
# The Unlimited Average Calculator
# Written in Pure Python.
# There is no existing bug I know and I tested everything myself.
# Feel free to like it and it's licensed under the MERIICISTYLE CORP. LICENSE


# The your and average section where we define the loop and the average at the beginning.
tour = 0
average = 0

# That's where we print the 'Welcome to our Tool Message and we explain them how the tool works.
print("""        
        Ortalama Hesaplayıcısına Hoş geldiniz.
        Seçimler aşağıdaki gibidir:
        Sayıları girerek enterladığınızda hepsi
        listeye eklenecek ve 0'a bastığınızda ortalamayı
        verir.
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
            if (type(sum(list))==int):
                print(sum(list) / int(len(list)))
            if (type(sum(list))==float):
                print(sum(list) / float(len(list)))
            break
        list.append(int(num))
        tour += 1

        print(list)
