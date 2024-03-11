print("Advanced things in python\n============================================")

# Decorators
print("\n[DECORATORS]")

def func(f):
    def wrapper(*args, **kwargs): 
        print("Started")
        rv = f(*args, **kwargs) # Pass in different amount of args or kwargs
        print("Finished\n")
        return rv

    return wrapper

@func # func2 = func(func2)
def func2(x):
    print("Hello from func2")
    print(f"{x} + 2 = {x+2}")
    return x

@func # func3 = func(func3)
def func3():
    print("Hello from func3")

z = func2(4)
func3()

print(z)


# Timer decorator
print("\n[TIMER DECORATOR]")

import time # Import time

# Timer decorator function
def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        total = time.time() - start

        print(f"Total execution time of function '{f.__name__}': {total}")
        return rv

    return wrapper

# Function to check
@timer
def test(nums):
    for _ in range(nums):
        pass

# Another function to check
@timer
def test2(num):
    time.sleep(num)

test(100000000)
test2(2)


# Call check decorator
print("\n[CALL CHECK DECORATOR]")

def called(f):
    def wrapper(*args, **kwargs):
        print(f"Function '{f.__name__}' has been called :)")
        f(*args, **kwargs)
        print("")

    return wrapper

@called
def check(x, y):
    print("Hello World!", x + y)

check(2, 8)
check(89, 15)
check(10, 124)