# Comparison Operators
# == - Equal to
# != - Not equal to
# > - Greater than
# >= - Greater than or equal to
# < - Less than
# <= - Less than or equal to

# Basic Conditional Example
num = 5

if num >= 5:
    print("num is large")

elif num >= 3:
    print("num is between 3 and 5")

else:
    print("num is small")

# Conditionals with Logic Statements
sunny = False
hungry = False

if sunny and hungry:
    print("Go out to eat")

elif not sunny and hungry:
    print("Stay home and cook")

else:
    print("Do nothing")

# For Loop that goes from 20 to 40 and counts by 9's
for i in range(20, 40, 9):
    print(i)

print("a" * 10)

num = 5
while num > 0:
    num -= 1
    print(num)

print("Finished")

a = input("> ")
while a != "":
    print("- " + a)
    a = input("> ")
