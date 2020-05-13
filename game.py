import random

def pick_random_word():
    word = ['flower','pen','mobile','laptop','pencil','soccer','football']
    index = random.randint(0,len(word)-1)
    return word[index]


def checkCharacter(default_word,character,current_word):
    modified_word = ""
    for i in range(len(default_word)):
        if default_word[i] == character and default_word[i] == "_" :
            modified_word += character
        else:
            modified_word +=current_word[i]
    return modified_word

def PrintCurrentWord(current_word,attempts):
    print("Current State :", end = " ")

    for i in current_word:
        print(i,end = " ")
    print(" attempts remaining",end = " ")
    print(attempts)

def current_word_status(default_word,character,attempts,current_word):
    if character in default_word:
        current_word_status = checkCharacter(default_word,character,current_word)
    else :
        attempts = attempts-1
    return current_word,attempts

def results(default_word,current_word,attempts):
    if current_word == default_word:
        print("Congratulation, You Won")
        return True
        
    if attempts <=0 :
        print("You lost")
        print("Word Was")
        print(default_word)
        return True
    return False

def play_game(attempts = 5):
    default_word = pick_random_word()
    current_word = "_" * len(default_word)
    attempts_remaining = attempts
    PrintCurrentWord(current_word,attempts)
    while (True) :
        character = input("Guess a character")
        #character default_word me hai?
        current_word, attempts_remaining = current_word_status(default_word,character,attempts_remaining,current_word)

        PrintCurrentWord(current_word,attempts_remaining)

        game_ended = results(default_word,current_word,attempts_remaining)

        if game_ended:
            break


play_game()