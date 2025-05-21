# Import all modules
import random
from hangman_words import word_list
import hangman_art

# Import hangman AHCII logo
print(hangman_art.logo)

# Specify number of lives and randomize the chosen word
lives = 6

chosen_word = random.choice(word_list)

# Specify placeholder as blank lines for letters that need to be guessed
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

# Make sure user can keep guessing words until game is over and show how many lives left
game_over = False
correct_letters = []

while not game_over:

    print("****************************" + str(lives) + " LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed " + guess + ", try again.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
          
# Show which letter user still needs to guess
    print("Word to guess: " + display)

# Making sure user loses lives for wrong guesses and specify when game is over
    if guess not in chosen_word:
        print("You guessed " + guess + " ,that is not in the word, you lose a life.")
        lives -= 1
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    elif lives == 0:
        game_over = True
        print("The word you had to guess was " + chosen_word)
        print(f"***********************YOU LOSE**********************")

    print(hangman_art.stages[lives])
