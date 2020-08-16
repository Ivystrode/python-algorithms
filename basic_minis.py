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

# with open("word_list.txt", "r") as f:
#     word_list_file = f.readlines()

# strength = int(input("On a scale of 1-5, how strong do you want your password to be?\n"))



# lchars_str = "qwertyuiopasdfghjklzxcvbnm"
# nums_str = range(0, 10)
# syms_string = "!£$%^&*()_+=-[]}{;'#~@:<>?/.,|\`¬'}"

# word_list = [word.strip() for word in word_list_file]
# lchars_list = [char for char in lchars_str]
# allchars_list = lchars_list + [char.upper() for char in lchars_list]
# nums_and_chars_list = allchars_list + [str(num) for num in nums_str]
# all_symbols_list = nums_and_chars_list + [symbol for symbol in syms_string]

# if strength == 1:
#     password = random.choice(word_list) + random.choice(word_list)
# elif strength == 2:
#     password = ''.join(random.sample(lchars_list, 7))
# elif strength == 3:
#     password = ''.join(random.sample(allchars_list, 11))
# elif strength == 4:
#     password = ''.join(random.sample(nums_and_chars_list, 16))
# elif strength == 5:
#     password = ''.join(random.sample(all_symbols_list, 24))
# else:
#     print("select a number from 1-5")
    

# print(password)#

def tower_builder(n_floors):
    """Returns a list where each element is the number of asterisks of the floor number...should appear stacked like a tower"""
    tower = []
    spacing = n_floors - 1
    stars = 1
    for i in range(0, n_floors):
        tower.append(" " * spacing + "*" * stars + spacing * " ")
        stars += 2
        spacing -= 1
    return tower

def tower_builder_lite(num_floors):
    return [("*" * (i*2-1)).center(num_floors*2-1) for i in range(1, num_floors+1)]


    # return [("*"*i).center(n_floors, " ") for i in range(1, n_floors+1)]

print(tower_builder(7))
print("===")
print(tower_builder_lite(7))