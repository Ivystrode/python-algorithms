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
hidden_word = list(secret_word)
word = list('*'*secret_word_length)

def char_checker(guess):
    global word
    global hidden_word
    global guesses

    if guess in all_guesses:
        print("You've already guessed that one!")
        time.sleep(2)

    else:
        all_guesses.append(guess)
        if guess in hidden_word:

            for i, char in enumerate(hidden_word):
                if char == guess:
                    word[i] = guess

        else:
            guesses += 1
            print(f"incorrect - wrong guesses: {guesses}")

print("Let's play Hangman!")
print("Your word to guess: ")

while playing:
    time.sleep(1)
    print(''.join(word))

    if ''.join(word) == secret_word:
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
        print("You lose")
        print("The answer was " + secret_word)
        playing = False


