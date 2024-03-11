print("Intermediate things in python\n============================================")

# Maps
print("\n[MAPS]")

lst = [i for i in range(1, 21)]
power_func = lambda x: x**2

print("Map:", list(map(power_func, lst)))
print("Comprehension:", [power_func(x) for x in lst], "\n") # Same thing


num_lst = [i for i in range(1, 21)]
add_func = lambda x: x + 10

print("Map:", list(map(add_func, num_lst)))
print("Comprehension:", [add_func(x) for x in num_lst]) # Same thing