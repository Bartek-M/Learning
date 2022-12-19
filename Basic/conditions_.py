print("Basic things in python\n============================================")

# Booleans conditions
print("\n[BOOLEAN CONDITIONS]")
"""
Condtions in python
| ==    equal to
| !=    not equal to
| >=    greater or equal to
| <=    less or equal to
| >     more then
| <     less then
"""

a = 8
print(f"{a} is equal to 8 | ", a == 8) # True
print(f"{a} is equal to 2 | ", a == 2) # False
print(f"{a} is not equal to 3 | ", a != 3) # True
print(f"{a} is smaller or equal to 9 | ", a <= 9) # True
print(f"{a} is bigger or equal to 24 | ", a >= 24) # False


# And, or, not
print("\n\n[AND, OR, NOT]")

a, b = 0, 0 # False, False
a1, b1 = 1, 1 # True, True

print("AND") # Everything must be True
print(f"{a} and {b} = {a and b}") # False
print(f"{a1} and {b} = {a1 and b}") # False
print(f"{a} and {b1} = {a and b1}") # False
print(f"{a1} and {b1} = {a1 and b1}") # True

print("\nOR") # At least one must be True
print(f"{a} or {b} = {a or b}") # False
print(f"{a1} or {b} = {a1 or b}") # True
print(f"{a} or {b1} = {a or b1}") # True
print(f"{a1} or {b1} = {a1 or b1}") # True

print("\nNOT") # False <-> True
print(f"not ({a} and {b}) = {int(not (a and b))}") # True
print(f"not ({a1} and {b1}) = {int(not (a1 and b1))}") # False
print(f"not ({a} or {b}) = {int(not (a or b))}") # True
print(f"not ({a1} or {b1}) = {int(not (a1 or b1))}") # False


# If, Elif, Else
print("\n\n[IF, ELIF, ELSE]")

inpt = input("Chose a random number: ") # int(input()) can be used as well

if int(inpt) % 2 == 0: 
    print("Your number is even")
else: 
    print("Your number is odd") 


inpt_1 = input("\nWhich IDE for python is the best? [VS Code, Atom, PyCharm, IDLE, Notepad] ").lower()

if inpt_1 == "vs code": 
    print("That's very good IDE, I am using the same one :)")
elif inpt_1 == "atom": 
    print("Hmm, that's from github. It looks good, but I prefer vs code")
elif inpt_1 == "pycharm": 
    print("O, it' very complicated program. Do you know how to use it?")
elif inpt_1 == "idle":
    print("Python IDLE is very basic, but if you are a begginer it is great")
elif inpt_1 == "notepad":
    print("If I were you, I would consider diffrent one. Is it enough for you?") 
else: 
    print("You've got mistake, try again")


x = 2
y = 3 

if x == 4 or y == 3: 
    print("x = 4 or y = 3")
if x == 2 and y == 3:
    print("x = 2 and y = 3")

if x == 2:
    if y == 3:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")


inpt_2 = input("2 + 2 = 4? [y/n] ").lower()

if inpt_2 != "y" and inpt_2 != "n": # Inpt_2 is neither y and n
    print("Wrong answer, it should be y or n")
if inpt_2 == "y" or inpt_2 == "n": # Inpt_2 is correct, either y or n
    print("Your answer is either y or n")

if inpt_2 == "y": # Picked y
    print("Your answer is correct")
elif inpt_2 == "n": # Picked n
    print("Your answer is incorrect")
else: # Picked something else
    print("Wrong input")