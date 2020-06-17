while True:
    import datetime
    name = input("Your Name: ")
    age = input("Your Age: ")
    birth = int(datetime.datetime.today().year - int(age))
    year = birth + 100

    print(name + " you will be 100 years old in year " + str(year) + ".")