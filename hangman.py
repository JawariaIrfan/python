logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
word = ['apple','orange','banana','advark','carrot']
choice = random.choice(word)
answer = print(f"the choose word is {choice}")
#guess = input('guess a letter ').lower()
# for char in choice:
#     if char in guess:
#         print("right")
#     else:
#         print("wrong")
display = []
for letter in choice:
    display.append("_")
#print(display)
# for position in range(len(choice)):
#     letter = choice[position]
#     if letter == guess:
#          display[position] = letter
#          print(display)


# for position in range(len(choice)):
#     while display[position] == "_":
#         guess = input(" guess a letter ")
#         letter = choice[position]
#         if letter == guess:
#             display[position] = letter
#             print(display)
#         else:
#             print("nope, wrong answer")
# else:
#         print("you win!")
lives = 6
end_of_game = False

while not end_of_game:
    guess = input(" guess a letter ")
    if guess in display:
        print("you have already chosen the word")
    for position in range(len(choice)):
        letter = choice[position]
        if letter == guess:
                display[position] = letter
        
    print(display)

    if guess not in choice:
        print(f"you choose the word {guess}, that's not in the word, try again idiot")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose dumbass")
        
    # if "_" not in display:
    #     end_of_game = True
    #     print("you win!")
    print(stages[lives])
