'''
.upper
.lower
.find
.count
.split
.replace
.strip
.isupper
.islower
'''

# String and List Methods

my_str = " Hello World "
my_list = list(my_str) # [' ', 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', ' ']

print(my_str.lower()) # hello world
print(my_str.upper()) # HELLO WORLD

print(my_str.find("e")) # 2
print(my_str.find("l", 5)) # 10

print(my_str.count("o")) # 2

print(my_str.split(" ")) # ["", "Hello", "World", ""]

print(my_str.replace("l", "a")) #  Heaao Worad

print(my_str.strip()) # Hello World

print("A".isupper()) # True
print("a".islower()) # True

for i in my_str:
    print(i, i.isupper(), i.islower())

# Returns
'''
a False True
H True False
e False True
l False True
l False True
o False True
  False False
W True False
o False True
r False True
l False True
d False True
a False True
'''

print(my_str[2]) # H
print(my_list[2]) # H

print(my_str[2:8]) # ello W
print(my_list[2:8]) # ['e', 'l', 'l', 'o', ' ', 'W']

print(my_str[:8], my_str[8:]) #  Hello W orld
print(my_list[:8], my_list[8:]) # [' ', 'H', 'e', 'l', 'l', 'o', ' ', 'W'] ['o', 'r', 'l', 'd', ' ']

print(my_str[2:10:2]) # el o
print(my_list[2:10:2]) # ['e', 'l', ' ', 'o']

print(my_str[10:2:-1]) # lroW oll
print(my_list[10:2:-1]) # ['l', 'r', 'o', 'W', ' ', 'o', 'l', 'l']

# List Methods

my_list = [4, 1, 5, 5, 11, 9, 11, 10]
my_list2 = [2, 4, 9, 7, 9]

print(my_list.count(5)) # 2

print(my_list.index(5)) # 2
print(my_list.index(11, 5)) # 6

my_list.extend(my_list2)
print(my_list) # [4, 1, 5, 5, 11, 9, 11, 10, 2, 4, 9, 7, 9]

print(my_list + my_list2) # [4, 1, 5, 5, 11, 9, 11, 10, 2, 4, 9, 7, 9]

# Functions

def greet():
    print("Hello!")
    how_are_you = input("How are you? ")
    print("That's great!")

greet()

def greet(name):
    print(f"Hello {name}!")
    how_are_you = input(f"How are you, {name}? ")
    print("That's great!")

greet("John")

def is_even_sum(num1, num2):
    if (num1 + num2) % 2 == 0:
        print("even")

    else:
        print("odd")

is_even_sum(6, 7)

def is_even_sum(num1, num2):
    if (num1 + num2) % 2 == 0:
        return True

    else:
        return False

check = is_even_sum(6, 7)
if check:
    print("even")

else:
    print("odd")

def is_even_sum(num1, num2):
    if (num1 + num2) % 2 == 0:
        return "even"

    else:
        return "odd"

print(is_even_sum(6, 7))
