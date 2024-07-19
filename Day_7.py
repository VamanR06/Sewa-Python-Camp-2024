# Reverse String

def reverse_string(string):
    return string[::-1]

user_input = input("Enter a phrase: ")
print(f"Reversed String: {reverse_string(user_input)}")

# Max of 3 Numbers

def max_of_3(num, num2, num3):
    if num > num2 and num > num3:
        return num

    elif num2 > num and num2 > num3:
        return num2

    else:
        return num3

numbers = input("Enter 3 numbers separated by commas: ").replace(" ", "").split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(max_of_3(numbers[0], numbers[1], numbers[2]))

# Uppercase Lowercase Finder

def upper_lower_counter(string):
    upper = 0
    lower = 0
    other = 0

    for i in string:
        if i.isupper():
            upper += 1

        elif i.islower():
            lower += 1

        else:
            other += 1

    return upper, lower, other

my_str = input("Enter a phrase: ")
upper, lower, other = upper_lower_counter(my_str)

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
print(f"Other: {other}")

# Prime Checker

def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return "composite"

    return "prime"

num = int(input("Enter a number: "))
print(f"{num} is {is_prime(num)}")

# Error Handling

# Basic Error Handling
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid number")

# Continuous Error Handling
is_valid = False
while not is_valid:
    try:
        num = int(input("Enter a number: "))
        is_valid = True

    except ValueError:
        print("Invalid number")

# File Handling

# Reading a File
file = open("test.txt")
print(file.read())
file.seek(0) # Make sure to reset cursor position
print(file.read())
file.close()

# Write to a File (erases all data inside it)
file = open("test.txt", "w")
file.write("Hello")
file.close()

file = open("test.txt")
print(file.read())
file.close()

# Append to a File (adds on data)
file = open("test.txt", "a+")
file.write(" World")
file.seek(0)
print(file.read())
file.close()

# Reads Lines of a File
file = open("test.txt")
print(file.readlines(20))
file.seek(0)

data = file.readlines()
for i in data:
    print(i)
