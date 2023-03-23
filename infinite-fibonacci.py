def fibonacci_numbers():
    """Infinite Generator for fibonacci numbers starting at 0.
    >>> fibs = fibonacci_numbers()
    >>> next(primes)
    0
    >>> next(primes) # Second call
    1
    >>> next(primes) # Third call
    1
    >>> next(primes) # Fourth call
    2
    >>> next(primes) # Fifth call
    3
    """
    next = 0
    after = 1
    while True:         # (a)
        yield next      # (b)
        temp = next + after
        next = after    # (c)
        after = temp    # (d)

print(fibonacci_numbers()) # <generator object fibonacci_numbers at 0x7f9b1c0b9f68>
fibs = fibonacci_numbers()
print(next(fibs)) # 0
print(next(fibs)) # 1
print('---')
fibs = fibonacci_numbers()
for i in range(10):
    print(next(fibs))

print(next(fibs)) # 55