print("Intermediate things in python\n============================================")

# Comprehensions
print("\n[COMPREHENSIONS]")

nums = [i for i in range(15)]
print("Generated nums <0; 15):", nums)

even = [i for i in range(30) if i % 2 == 0]
print("Even nums <0; 30)", even)

nested_list = [[i for i in range(4)] for _ in range(4)]
print("Nested list:", nested_list)