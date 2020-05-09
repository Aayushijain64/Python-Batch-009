#Storing numerous records
student1 = 20
student2 = 30
student3 = 40

students = [20,30,40,50,4,3,1,2,7,4,3,21,1,8,9,5,4,3,2,7]
print(students[0])
#Back Iteration
print(students[-3])
#change value of third place
pos = int(input())
marks = int(input())
students[pos] = marks
print(students)
#print records according to names
students_name =[['Aayushi',30],['Tanvi',90],['Devashish',100]]
print(students_name)
#different type of list
students_type = [20,30,'disqualified',50,'bad',60]
print(students_type[2])
#user initialised list
list1 = []
for i in range(0,5):
    num = int(input())
    list1.append(num)
print(list1)
#Delete an element in list
del(students[2])
print(students)
#slicing of list
print(students[0:5])
#remove 3
for i in students:
    if i == 3:
        pos = i
        break
del(students[pos+1])
print(students)