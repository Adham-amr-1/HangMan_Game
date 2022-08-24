from words import word_list
import random


print('------------------------')
print('Welcome To HangMan Game')
print('------------------------')

wordDictionary = word_list
randomword = random.choice(wordDictionary)

for x in randomword:
    print('_', end=' ')

def print_hangman(wrong):
    if   (wrong == 0) :
        print('\n+----+')
        print('       |')
        print('       |')
        print('       |')
        print('      ===')
    elif (wrong == 1) :
        print('\n+----+')
        print(' O      |')
        print('        |')
        print('        |')
        print('       ===')
    elif (wrong == 2) :
        print('\n+----+')
        print(' O      |')
        print(' |      |')
        print('        |')
        print('       ===')
    elif (wrong == 3) :
        print('\n+----+')
        print(' O      |')
        print('/|      |')
        print('        |')
        print('       ===')
    elif (wrong == 4) :
        print('\n+----+')
        print(' O      |')
        print('/|\     |')
        print('        |')
        print('       ===')
    elif (wrong == 5) :
        print('\n+----+')
        print(' O      |')
        print('/|\     |')
        print('/       |')
        print('       ===')
    elif (wrong == 6) :
        print('\n+----+')
        print(' O      |')
        print('/|\     |')
        print('/ \     |')
        print('       ===')

def printword(guessword):
    counter      = 0
    rightletters = 0
    for char in randomword:
        if(char in guessword):
            print(randomword[counter], end=' ')
            rightletters += 1
        else:
            print(' ', end=' ')
        counter += 1
    return rightletters

def printlines():
    print('\r')
    for char in randomword:
        print('\u203E', end=' ')

lenght_of_word_to_guess = len(randomword)
amount_times_wrong = 0
current_guess_index = 0
current_letter_guessed = []
current_letter_right = 0

while (amount_times_wrong != 6 and current_letter_right != lenght_of_word_to_guess):
    print('\nLetters guessed so far: ')
    for letter in current_letter_guessed:
        print(letter, end=' ')
    
    letterGuessed = input('\nGuess a Letter: ') 
    
    if (randomword[current_guess_index] == letterGuessed):
        print_hangman(amount_times_wrong)
        
        current_guess_index += 1
        current_letter_guessed.append(letterGuessed)
        current_letter_right = printword(current_letter_guessed)
        printlines()
    else:
        amount_times_wrong += 1
        
        current_letter_guessed.append(letterGuessed)
        
        print_hangman(amount_times_wrong)
        
        current_letter_right = printword(current_letter_guessed)
        printlines()

print('\n---------------------------')
print('\nGame is Over Thank You <3  ')
print('-----------------------------')
