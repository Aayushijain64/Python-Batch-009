#2D list
students = [['Aayushi',34],['Jayshree',65]]
#Dictionary
#Key-Value Pair
students1 = {
    '1' : 'Aayushi Jain' ,
    '2' : 'Yashi Pandey',
    '3' : 'Jayshree',
    '4' : 'Yash'
}
print(students1)
print(students1['1'])
# Keys Should be unique 

#Printing all the keys
print(students1.keys())
List1 = []
List1.append(students1.keys())
print(List1)
del students1['2']
print(students1)