total = input("Enter number to fizzbuzz up to ")

print(int(total))


#METHOD 1
for num in range(1, int(total)):
    if num % 3 == 0 and not num % 5 == 0:
        print("fizz")
    elif num % 5 == 0 and not num % 3 == 0:
        print("buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print(num)

nexttotal = input("Method 2. Enter a number.")

def divbyboth(number):
    if number % 3 == 0 and not number % 5 == 0:
        print("fizz")
    elif number % 5 == 0 and not number % 3 == 0:
        print("buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)

def fizzbuzz(x):
    for i in range(1, int(x)):
        divbyboth(i)

fizzbuzz(nexttotal)