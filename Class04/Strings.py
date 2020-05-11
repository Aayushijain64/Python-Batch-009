#Concatenation of strings
string1 = "Aayushi "
string2 = "Jain"
string3 = string1 + string2
print(string3)

#Finding Character in String
Inp = "Python Programming"
ctr = 0
for i in Inp :
    if i == 'o' :
        flag = 1
        break
    else :
        ctr+=1
    
if flag == 1:
    print ("true")
    print(ctr)
else:
    print("False")

#Inbuit COmmand
print(Inp.find("o"))
