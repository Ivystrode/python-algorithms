import random

# #==========Print if num less than 5==========

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [num for num in a if num < 5]

# print(b)

# print("===================")

# #==========List of nums that are divisors of c==========

# # c = input("choose a number: ")

# x = range(1, int(c)+1)

# y = [n for n in x if int(c) % n == 0]

# # print(y)

# print("===================")

#==========Password gnerator==========

with open("word_list.txt", "r") as f:
    word_list_file = f.readlines()

strength = int(input("On a scale of 1-5, how strong do you want your password to be?\n"))



lchars_str = "qwertyuiopasdfghjklzxcvbnm"
nums_str = range(0, 10)
syms_string = "!£$%^&*()_+=-[]}{;'#~@:<>?/.,|\`¬'}"

word_list = [word.strip() for word in word_list_file]
lchars_list = [char for char in lchars_str]
allchars_list = lchars_list + [char.upper() for char in lchars_list]
nums_and_chars_list = allchars_list + [str(num) for num in nums_str]
all_symbols_list = nums_and_chars_list + [symbol for symbol in syms_string]

if strength == 1:
    password = random.choice(word_list) + random.choice(word_list)
elif strength == 2:
    password = ''.join(random.sample(lchars_list, 7))
elif strength == 3:
    password = ''.join(random.sample(allchars_list, 11))
elif strength == 4:
    password = ''.join(random.sample(nums_and_chars_list, 16))
elif strength == 5:
    password = ''.join(random.sample(all_symbols_list, 24))
else:
    print("select a number from 1-5")
    

print(password)