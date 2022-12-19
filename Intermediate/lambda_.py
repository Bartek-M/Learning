print("Intermediate things in python\n============================================")

# Lambda
print("\n[LAMBDA]")

is_even = lambda x: x % 2 == 0
print("Number 8 is even:", is_even(8))
print("Number 7 is even:", is_even(7))


power = lambda x, y=2: x ** y
print("\n8 ^ 2 =", power(8))
print("2 ^ 3 =", power(2, 3))