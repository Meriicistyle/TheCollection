
listy=list(map(int,input("Enter the numbers separated by spaces: ").split()))

def findgcd(x, y):
   while(y):
      x, y = y, x % y
   return x
num1 = listy[0]
num2 = listy[1]
gcd = findgcd(num1,num2)
for i in range(2,len(listy)):
   gcd = findgcd(gcd,listy[i])
print("Greatest common divisor is ", gcd)