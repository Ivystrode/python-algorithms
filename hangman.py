import random
import time

# ==========Extract from file==========
# Extract the words from word_list.txt and insert them into a list

word_list = []

with open('word_list.txt', 'r') as word_list_file:
    for line in word_list_file:
        line = line.strip()
        word_list.append(line)

# ==========Game initialisation==========
# Randomly select a word from word_list and initialise all game attributes

secret_word = random.choice(word_list)

playing = True
guesses = 0
all_guesses = []
word_characters = list(secret_word)
displayed_word = list('*'*len(secret_word))

print("Let's play Hangman!")
time.sleep(2)
print("Pick a letter, or type 'guesses' to see what you've already guessed")
time.sleep(2)
print("\n")

# ==========Input processing==========
# Check the letter the user has picked to see if it is in the secret word

def char_checker(guess):
    global guesses

    if guess in all_guesses:
        print("You've already guessed that one!")
        time.sleep(1)

    else:
        all_guesses.append(guess)

        if guess in word_characters:
            for i, char in enumerate(word_characters):
                if char == guess:
                    displayed_word[i] = guess

        else:
            guesses += 1
            print(f"incorrect - wrong guesses: {guesses}/7")


# ==========Game Loop==========
# Prompt the user to choose a character and check it off against the secret word.
# Terminates the script if user uses up their 7 guesses or if they get the word.
# Uses the sleep function to be slightly enhance user experience

while playing:
    time.sleep(1)
    print("Word: " + ''.join(displayed_word))

    if ''.join(displayed_word) == secret_word:
        print("Congratulations you win")
        playing = False
        break

    if guesses < 7:
        guess = input("Please enter your next guess: ")
        guess = guess.lower()

        if guess == secret_word:
            print("Congratulations you win")
            playing = False

        elif guess == "guesses":
            print("Guesses so far:")
            print(all_guesses)

        else:
            char_checker(guess)
    else:
        print("The answer was " + secret_word)
        print("You lose")
        playing = False


