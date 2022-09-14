
from random import choice

words = ['teacher', 'shark', 'computer', 'chocolate','coriander'] 
right_letters = [] 
wrong_leters = [] 
attempts = 6 
hits = 0 
end_game = False 

def choose_word(list_words):
    choosen_word =choice(list_words)
    unique_letters = len(set(choosen_word))
    
    return choosen_word,unique_letters

def ask_letter():
    """Ask letter from the alphabet"""
    choosen_letter = ''
    valid_letter = False
    alphabet='abcdefghijklmnopqrstuvwxyz'
    
    while  not valid_letter:
        choosen_letter= input('pick one letter: ')
        if choosen_letter in alphabet and len(choosen_letter) == 1:
            valid_letter= True
        else:
            print(' The letter you have choosen is incorrect ')
    return choosen_letter





def show_new_board(choosen_word):
    """shows the board game and the length of the word"""

    hiden_list= []
    
    for l in choosen_word:
        if l in right_letters:
            hiden_list.append(l)
        else:
            hiden_list.append('-')
    print(' '.join(hiden_list))
    



def check_letter(choosen_letter,hiden_word,life,coincidences ):
    """"checks if the letter is in the word.
   if is not in the word takes one from the total life 
   """
    end =False
    
    if choosen_letter in hiden_word:
        right_letters.append(choosen_letter)
        coincidences +=1
    else:
        wrong_leters.append(choosen_letter)
        life -=1
    if life == 0:
      end = gameOver()
    elif coincidences == unique_letters:
        end = win(hiden_word)
        
    return life, end, coincidences
        
        
def gameOver():
    print(' you have run out of life')
    print ('the secret word it was' + word)   
        
    return True

def win(discovered_word):
    show_new_board(discovered_word)
    print('congratulations, you find the word')
    
    return True
    
word, unique_letters = choose_word(words)

while not end_game:
    
    print('\n'+ '*' *20 + '\n')
    print(' Hello, do you want to play hangman')
    print('\n')
    show_new_board(word)
    print('\n')
    print(('wrong letters: ') + '-'.join(wrong_leters))
    print(f'life: {attempts}')
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    
    attempts, finish, hits = check_letter(letter,word,attempts,hits)
    
    end_game = finish


