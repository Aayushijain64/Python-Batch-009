#Odd Even
num1 = int(input("Enter any value"))
if(num1 % 2 == 1):
    print("The number is odd")
else:
    print("even number")

#If a number is divisible by 5 print "Wired", divisible by 10 & 5 print " Wireless" else, print "Not wired"

num = int (input())
if(num % 5 == 0 and num% 10 ==0):
    print("Wireless")
elif(num %5 ==0):
        print("Wired")
else:
    print("Not Wired")