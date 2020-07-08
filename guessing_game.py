number_known = False
guesses = 0
first_guess = 50

def guess(number):
    print("Is your number " + str(number))
    user_response = input("enter 'yes' if correct, or 'higher' or 'lower': \n")
    return user_response

def guess_stages(my_guess):
    my_guess = first_guess
    global guesses
    global number_known
    while number_known != True:
        answer = guess(my_guess)
        if answer == 'higher':
            


            my_guess += 1
            guesses += 1
        elif answer == 'lower':
            my_guess -= 1
            guesses += 1
        elif answer == 'yes':
            number_known = True
            print("your number was " + str(my_guess) + ". That took me " + str(guesses) + " guesses.")
        else:
            print("Unknown input")



guess_stages(first_guess)

