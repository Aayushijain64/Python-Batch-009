import numpy as np
import math 

#Declaration and printing of Array
x1 = np.array ([[2,3,4],[5,6,7]],float) 
print(x1)
#to print element 6
print(x1[1,1])
#Type of x1
print(type(x1))
# 2 3 4    
# 5 6 7
#To check the shape of array x1
print(x1.shape)

x3 = np.array ([[1],[2],[3]])
print(x3.shape)

x2 = np.array([[1,2,3]])
print(x2.shape)
x2 = np.transpose(x2)
print(x2.shape)
#Matrix Addition
#print(x1+x2)
print("\n")
print(x1)
print("\n")

#Multiplication
#print(x1 * x2)
print("\n")
#Matrix Multiplication
print(np.dot(x1,x2))


y1 = [[2,3,4],[5,6,7]]
y2 = [[1,2,3],[4,5,6]]
print(y1[0][0])
print(y1 +y2)


#Identity matrix  - eye -> Identity Matrix
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(I)

I1 = np.eye(3,3)
print(I1)

# Zero Matrix
Z = np.zeros((3,3),int)
print(Z)

#one Matrix
O = np.ones((3,3),int)
print(O)

#Constant Matrix
F = np.full((3,3),10,int)
print(F)

#Reverse of Array
array = np.array([1,2,3,4],float)

print (array[::-1])

#reshape of array
print(array.reshape(2,2))