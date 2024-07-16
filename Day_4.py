# Pyramid Maker
rows = int(input("Enter how many rows: "))

for i in range(1, rows+1):
    print("# " * i)

# Add Up Numbers (without break)
total = 0
num = int(input("Enter a number: "))

while num != -1:
    total += num
    num = int(input("Enter a number: "))

print(f"Total: {total}")

# Add Up Numbers (with break)
total = 0
num = int(input("Enter a number: "))

while True:
    if num == -1:
        break
    
    total += num
    num = int(input("Enter a number: "))

print(f"Total: {total}")


# Factorial Calculator (without continue)
total = 1

num = int(input("Enter a number: "))

for i in range(1, num+1):
    total *= i

print(f"{num}! = {total}")


# Factorial Calculator (with continue)
total = 1

num = int(input("Enter a number: "))

for i in range(num+1):
    if i == 0:
        continue

    total *= i

print(f"{num}! = {total}")

# Picking a random number
import random

answer = random.randint(1, 100)

print(answer)

