print("Advanced things in python\n============================================")

# Generators
print("\n[GENERATORS]")

"""
This will fill up all of your memory

x = [i**2 for i in range(1000000000000)]

for el in x:
    print(el)


This will work, but it's long

class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        
        return rv

g = Gen(1000000000000)

while True:
    try:
        print(next(g))
    except StopIteration:
        print("\n[FINISHED]")
        break
"""

def gen(n):
    for i in range(n):
        yield i**2

g = gen(10000)

for num in g:
    print(num)