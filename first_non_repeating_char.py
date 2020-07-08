string = input("Enter string\n")
print(string)

d = {}

for char in string:
    d[char] = 0

for key, value in d.items():
    for char in string:
        if char == key:
            d[char] += 1

for key, value in d.items():
    if value == 1:
        print(str(key) + " appears " + str(value) + " time/s, and is the first to do so")
        break