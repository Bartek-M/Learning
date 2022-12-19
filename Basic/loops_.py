print("Basic things in python\n============================================")

#For loop
print("\n[FOR LOOPS]")

sum = 0
for i in range(5):
    sum += i
print(f"Your sum = {sum}\n")

for i in range(1, 4):
    print("Hi " + str(i), end="  |  ")
    if i == 3: print("")

for i in range(0, 6, 2):
    print(f"Even number: {i}", end="  |  ")


my_list = "DOG"

# First way of looping through string or list elements
print("\n\nFirst way of looping through string or list elements")
for i in range(len(my_list)): 
    print(i, my_list[i])

# Second way of looping through string or list elements
print("\nSecond way of looping through string or list elements")
for item in my_list: 
    print(my_list.index(item), item)

# Third way of looping through string or list elements
print("\nThird way of looping through string or list elements")
for index, value in enumerate(my_list):
    print(index, value)


# While loop
print("\n\n[WHILE LOOPS]")

x, y = 0, True
while y: # while condition is true, run a loop
    if x == 10:
        y = False
        print("x == 10\n")
    x += 1

sum = 0
while sum != 20: 
    sum += 1
print(f"Your sum = {sum}\n")

answ = ""
while answ != 4 and answ != 22:
    answ = int(input("2 + 2 = "))

    if answ == 4:
        print(f"Good answer, 2 + 2 = {answ}\n")
    elif answ == 22:
        print(f"If you consider 2 + 2 as string + string, then 2 + 2 = {answ}\n")
    else:
        print("Wrong answer, try again\n")

value, threshold = 0, 14
while value < threshold:
    if value == 4:
        print("Exiting loop at value = 4")
        break
    value += 1
else:
    print("Loop exited normally")