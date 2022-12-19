print("Intermediate things in python\n============================================")

# Filter
print("\n[FILTER]")

add_8 = lambda x: x + 8
is_odd = lambda x: x % 2 != 0

lst_a = [i for i in range(1, 21)]
lst_b = list(filter(is_odd, lst_a)) # Add to list only if func return True
lst_c = list(map(add_8, filter(is_odd, lst_a)))

print("Filtered odd numbers from list a:", lst_b)
print("Filterd list a and added 8:", lst_c)