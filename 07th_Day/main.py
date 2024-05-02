import random

from word_list import word_list
#Generate random word from our data list
computer_choice = random.choice(word_list)

word_length = len(computer_choice)

end_game = False
lives = 6

#Print Game Logo
from hangman import logo
print(logo)



#testing code by showing word

print("random word is : ",computer_choice)
#create blanks to guess how many words in this word

display = []

for blank in range(word_length):
    display += '_'

print("Letters in word :",display)

while not end_game:
    guess_word = input("Guess a letter : ").lower()


    # already in list
    if guess_word in display:
        print(f"You have already guessed {guess_word}")

    #Checking each word 
    
    for index in range(word_length):

        letter = computer_choice[index]

        if letter == guess_word:
            display[index] = letter
        

    #Wrong Guesses Control 
    if guess_word not in computer_choice:
        print("You guessed {guess}, it's not in the word.\nYou lose a life")

        lives -=1

        if lives == 0:
            end_game = True
            print("You lose the game")

        
    print(f"{' '.join(display)}")


    #Check no blank in Display : you win

    if "_" not in display:
        end_game = True

        print("You win the game")

    
    # Print Visual Display of how many lives you still have

    from hangman import stages

    print(stages[lives])