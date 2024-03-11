print("Basic things in python\n============================================")

# Lists
print("\n[LISTS]")

list_1 = ["List item 0", "List item 1", "List item 2", "List item 3", "List item 4", "List item 4", "List item 5", "List item 7"] # Define list

list_1.append("List item 8") # Add new item
list_1.insert(7, "List item 6") # Insert new item into 7th place
del list_1[0] # Remove first element 
list_1.pop(2) # Remove third element
list_1.remove("List item 4") # Remove first item with this value

print(list_1, "| List length:", len(list_1)) # Whole list
print(list_1[::-1], "\n") # Reverse

print(list_1.index("List item 1")) # Item index
print(list_1[0]) # Specific item
print(list_1[-1]) # Last item
print(list_1[2:len(list_1):2], "\n") # Every second character starting from index 2


list_2 = "Hello"
list_2 = list(list_2)
print(list_2)

list_2 = list_2[::-1]
string_list = "".join(list_2)
print(string_list)


list_3 = ["9", "8", "0", "2", "5", "4", "1"]
print("\n", list_3, sep="")
list_3.sort() # Sort list
print(list_3) 


# Dictionaries
print("\n\n[DICTIONARIES]")


# Tuples
print("\n\n[TUPLES]")


# Sets
print("\n\n[SETS]")