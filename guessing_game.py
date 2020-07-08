import time
import random

number_known = False
guesses = 0
hpn = int(input("Pick a number to be the maximum value: "))
lpn = 1
possibles = list(range(lpn, hpn+1))

gamechoice = input("Do you want to pick a random number or let the computer do it?\n")

def countdown(seconds):
    while seconds > 0:
        time.sleep(1)
        print(str(seconds) + "...")
        seconds -= 1


def guess(possibles, lpn, hpn, *args):
    global number_known
    global guesses
    while number_known == False:
        if args:
            mid = (hpn + lpn) // 2
            print("\nChecking " + str(mid))
            time.sleep(0.5) # not necessary, just so you can watch it work through it

            if mid < args[0]:
                lpn = mid
                print("Too low; guess higher")
                time.sleep(0.5) # not necessary, just so you can watch it work through it
                guesses += 1
                guess(possibles, lpn, hpn, target)
            elif mid > args[0]:
                hpn = mid
                print("Too high; guess lower")
                time.sleep(0.5) # not necessary, just so you can watch it work through it
                guesses += 1
                guess(possibles, lpn, hpn, target)
            else:
                time.sleep(0.5)
                print("Completed")
                print("Secret number is: " + str(mid))
                print("actual answer: " + str(target))
                print("That took " + str(guesses+1) + " guesses")
                number_known = True

        else:
            time.sleep(1)
            mid = (hpn + lpn) // 2
            answer = input("Is your number " + str(mid) + "\n")

            guesses += 1

            if 'yes' in answer:
                print("That took me " + str(guesses) + " guess/es to figure out")
                number_known = True
            elif 'higher' in answer:
                lpn = mid
                guess(possibles, lpn, hpn)
            elif 'lower' in answer:
                hpn = mid
                guess(possibles, lpn, hpn)
            else:
                print("Unknown input")

if 'user' in gamechoice or 'me' in gamechoice:
    print("Think of a number between 1 and " + str(hpn))
    countdown(5)
    guess(possibles, lpn, hpn)
else:
    target = random.choice(possibles)
    print("Secret number: " + str(target))
    print("Script will now try to guess what the secret number is")
    time.sleep(2)
    print("\n")
    time.sleep(1)
    guess(possibles, lpn, hpn, target)
