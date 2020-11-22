print("""
         This is the Least Common Multiple finder.
         To get results without errors, separate your
         numbers with spaces. For the result, of course
         click Enter. about 90 per cent is stolen code.
         """)

while True:
    listy = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    def findlcd(x, y):
        