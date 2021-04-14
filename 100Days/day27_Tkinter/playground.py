# '*' denotes an unlimited number of arguments...
def add(*nums):
    total = 0
    for num in nums:
        total += num
    print(f"Total = {total}")

add(3,2,4,6,2)

# '**' denotes an unlimited number of keyword arguments (or 'kwargs')
def calc(n, **kwargs):
    """Pass in as many keyword arguments as liked. In this case, 'n' is the initial value,
    and will execute whichever arguments that are intput in the kwargs."""
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(2, add=3, multiply=5)