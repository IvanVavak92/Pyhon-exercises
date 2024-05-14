import random
import hangman_art
import hangman_words

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed_letters = []

print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed letter: {guess}")

    guessed_letters += guess

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"The {guess} it's not in guessed word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(f"Lives: {lives}")
    print(hangman_art.stages[lives])
