print("Basic things in python\n============================================")

# Print
print("\n[PRINT STATEMENT]")

a = "Hello"
b = "World"
c = 8

print(a + " " + b) # Hello World
print(a * c) # HelloHelloHelloHelloHelloHelloHelloHello 
print(a, c) # Hello 8
print(a, c, sep=" World ") # Hello World 8

print(f"{a + b}!") # HelloWorld
print(f"{a} {c}\n") # Hello 8

print("Hello", end="\t")
print("World!") # Hello     World

print(f"""Hello
This is a test of
a print statement
2 + 2 = {2 + 2}""")


# Input
print("\n\n[INPUT FROM A USER]")

name = input("What's your name? ").capitalize()
age = input("How old are you? ") # int(input) can be used as well

print(f"\nNice to meet you {name}")
print(f"You were born in {2022 - int(age)}\n")


number = int(input("Pick a first number > "))
number_2 = float(input("Pick a second numebr, which should be a fraction > "))

print(f"\nSum of your numbers {number} + {number_2} = {number + number_2}")

input("\nPress ENTER to continue")