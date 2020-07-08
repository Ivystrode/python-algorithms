import time
import random

number_known = False
guesses = 0
hpn = 100000000
lpn = 1
possibles = list(range(lpn, hpn+1))
target = random.choice(possibles)

gamechoice = input("user pick number or random number?")


def guess(possibles, lpn, hpn, *args):
    global number_known
    global guesses
    while number_known == False:
        if target:
            mid = (hpn + lpn) // 2
            print("Checking " + str(mid))

            if mid < target:
                lpn = mid
                print("Guessing higher\n")
                guesses += 1
                guess(possibles, lpn, hpn, target)
            elif mid > target:
                hpn = mid
                print("Guessing lower\n")
                guesses += 1
                guess(possibles, lpn, hpn, target)
            else:
                print("Completed")
                print("Secret number is: " + str(mid))
                print("actual answer: " + str(target))
                print("That took " + str(guesses) + " guesses")
                number_known = True



        else:
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

if 'user' in gamechoice:
    print("Think of a number between 1 and 1,000,000")
    time.sleep(2)
    guess(possibles, lpn, hpn)
else:
    print("Secret number: " + str(target))
    print("Script will now try to guess what the secret number is")
    time.sleep(2)
    print("\n")
    time.sleep(1)
    guess(possibles, lpn, hpn, target)
