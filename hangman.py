import random
import time

word_list = []
playing = True

with open('word_list.txt', 'r') as word_list_file:
    for line in word_list_file:
        line = line.strip()
        word_list.append(line)

secret_word = random.choice(word_list)

guesses = 0
secret_word_length = len(secret_word)
all_guesses = []
word_characters = list(secret_word)
displayed_word = list('*'*secret_word_length)

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

print("Let's play Hangman!")
time.sleep(2)
print("Pick a letter, or type 'guesses' to see what you've already guessed")
time.sleep(2)
print("\n")
# print("Your word to guess: ")

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


