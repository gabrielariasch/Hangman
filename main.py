import random
import bank_of_words
import stages

game_on = True
chosen_word = random.choice(bank_of_words.words_list)

lives = 0
display = []

for letter in range(len(chosen_word)):
    display += "_"

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')

print("Welcome to Hangman! \n")

while game_on:
    print(display)
    guess = input("Guess a letter: ")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess.lower():
            display[position] = guess.lower()

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life")
        lives += 1

    print(stages.stages[lives])

    if lives == 6:
        game_on = False
        print("You lost! Thanks for playing!")


    x = "".join(display).lower()

    if x == chosen_word:
        game_on = False
        print("You WON! Thanks for playing!")
