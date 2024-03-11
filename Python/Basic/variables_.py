print("Basic things in Python\n============================================")

# Variables
print("\n[VARIABLES]")

"""
Variables in python:
| str() string: any text which is put in "" or ''; "Hello", 'test', "8"
| int() integer: any number; 2, 8, 51231
| float() float: any fraction number; 3.14, 2.5, 1393.3121
| bool() boolean: condition True or False
"""

string_1 = "hello"
string_2 = "2" + "0" 
integer_1 = 3 + 5
integer_2 = 15
bool_1 = True
bool_2 = False

print(f"String: '{string_1 + string_2}'")
print(f"String: '{string_1 + str(integer_1)}'")
print(f"Integer: {integer_1 + integer_2}")
print(f"Integer: {integer_2 + int(string_2)}")
print(f"Float: {integer_2 / integer_1}")

print(f"\nLength of a 'Hello World!' using len(): {len('Hello World!')}") # Len function only works on strings


# Changing strings
print("\n\n[CHANGING STRINGS]")

my_string = "testing STRING h3lLO"

print(my_string.lower()) # All lower case
print(my_string.upper()) # All upper case
print(my_string.capitalize()) # First letter is capitalized
print(my_string.title()) # Every first letter is capitalized

print("\n" + my_string.lower().replace("t", "[T]")) # Replacing characters
print(my_string.replace("h3lL", "Hell")) # Replacing characters

print("\nReversing:", my_string[::-1]) # Reverse


# Selecting characters
print("\n\n[SELECTING CHARACTERS]")

my_string_2 = "second testing STRING h3lLO"
my_numbers = "0123456789"

print("First character:", my_string_2[0]) # Get first character
print("Last character:", my_string_2[len(my_string_2)-1], "or", my_string_2[-1]) # Get last character

print("\nSpecific part:", my_string_2[7:15]) # Get specific part
print("Every second character:", my_numbers[0:len(my_numbers):2]) # Get every second character


# Formatting variables
print("\n\n[FORMATTING VARIABLES]")

my_text = "Hello World!"
my_num = 1234
my_float = 12.3456789

print(f"|{my_text:20s}|\n") # Put a string on 20 characters

print(f"LEFT    |{my_text:<20s}|") # Justify LEFT
print(f"RIGHT   |{my_text:>20s}|") # Justify RIGHT
print(f"CENTER  |{my_text:^20s}|\n") # Justify CENTER

print(f"|{my_num:07d}|") # Display int on 7 characters
print(f"|{my_float:07.3f}|") # Display float on 7 characters with 3 after .