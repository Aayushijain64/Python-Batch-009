#name to be printed times n times 
#begin pointer
#end pointer
#itertion pointer
n = int(input("Enter any no."))
name = input("Enter Your name")
for i in range(0,n):
    print(name)

#String is accepted by user, print all the letters
string = input("Enter any string")
for i in string:
    print(i,end=',')


#Approach 2
length = len(string)
for i in range(0,length,2):
    print(string[i])

#Approach3 : WRONG If else wont check repeatedly

#user accept1-10
#Approach 1
for i in range(1,10):
    if i==5 :
        break
    else:
        print(i,end='')
print("\nApproach2")
for i in range(1,10):
    if i==5 :
        continue
    else:
        print(i,end='')
#string = APPLE

#While LOOP Count 1-9
i=1
print("\n")
while(i<10):
    print(i,end='')
    i=i+1
print("\n")

#Nested Loops
#Print 2's table
for i in range(1,11):
    print(2*i)
#Print 1-5's table
#2 4 6 8
#3 6 9 12
for i in range(2,6):
    for j in range(1,11):
        print(i*j,end=' ')
    print("\n")

#Same Question With While
i = 2
while(i<6):
    j=1
    while(j<11):
        print(i*j,end=' ')
        j=j+1
    print("\n")
    i=i+1



