#Functions 
#User defined Functions
def add (a,b):
    c = a + b
    print(c)

def sub (a,b):
    c = a - b
    print(c)
def mul (a,b):
    c = a * b
    print(c)
def div (a,b):
    c = a / b
    print(c)

fun = input()
a = int(input())
b = int (input())
if fun == "add":
    add(a,b)
    #print (c)  : error without returning
elif fun == "sub":
    sub(a,b)
elif fun == "mul":
    mul(a,b)
else :
    div(a,b)


def add (a,b):
    c = a + b
    return(c)

def sub (a,b):
    c = a - b
    return(c)
def mul (a,b):
    c = a * b
    return(c)
def div (a,b):
    c = a / b
    return(c)
#Maths Equation input from user -and use variables in main 
# print (a+b)/c
a = int(input())
b = int (input())

c = add(a,b) 

d = int(input())
print (div(c,d)) 

#Inbuilt Functions 
#min
list1 =  [1,2,3,4,5]
minimum = +100000000000000000 
for i in list1 :
    if i <minimum :
        minimum =i
print (minimum)

#Inbuilt Functions
print(min(list1))
print(max(list1))