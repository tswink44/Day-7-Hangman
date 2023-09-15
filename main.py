import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear
lives = 6
chosen_word = word_list[random.randint(0, len(word_list)-1)]
display = []
guessed_letters = []
for letter in chosen_word:
    display.append("_")
print(logo)
print(display)

while "_" in display:

    guess = input("Guess a letter ")
    clear()
    guess_tracker = 0
    if guess in guessed_letters:
        print("Letter already guessed, try again")
        guess_tracker += 1
    else:
        guessed_letters.append(guess)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guess_tracker += 1

    if guess_tracker == 0:
        lives = lives-1
        print(stages[lives])
    if lives == 0:
        print("You lose")
        exit()
    print(display)
