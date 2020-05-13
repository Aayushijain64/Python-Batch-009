import random

#Random number generation
#print(random.randint (1,10))

word = ['Flower','pen','mobile','laptop','pencil','soccer','football']
index  =  random.randint(0,len(word)-1)
#print(word[index])
#print(len(word))
#print(word[0])


#Through Fuctions 
def pick_random_word(index = 2):
    word = ['Flower','pen','mobile','laptop','pencil','soccer','football']
    #index = random.randint(0,len(word)-1)
    return word[index]

print(pick_random_word(6))