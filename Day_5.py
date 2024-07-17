# List Methods
my_list = [1, "b", 3, "d", 5, "f"]

my_list.append(7)

my_list.remove("b")

my_list[1] = "hello"

print(my_list[3])

my_list.pop(3)

my_list.insert(3, 1000)

my_list.reverse()

print(my_list)

my_list2 = [345, 46, 3298, 13, 94, 10]

my_list2.sort()

print(my_list2)

# Looping Through List
for i in range(len(my_list2)):
    if my_list2[i] % 2 == 0:
        continue
    
    my_list2[i] *= 2

print(my_list2)


for i in my_list2:
    i *= 2

print(my_list2)

# Multiple Finder
multiples = []
max_num = int(input("Enter the max number: "))
multiple = int(input("Enter the number to find a multiple of: "))

for i in range(1, max_num+1):
    if i % multiple == 0:
        multiples.append(i)

print(multiples)

# String to List .split function
grades = input("Enter your grades: ").split(", ")

print(grades)
