#list[1,2,3,4,5,6,7,8,9,10]
#print all prime numbers
#output
#2 3 5 7 

#solve using inbilt functions
import sympy
import numpy as np
n = int(input())
print (sympy.isprime(n))
ranges = int(input())
print (list(sympy.primerange(0, ranges)))  
