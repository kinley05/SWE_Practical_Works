import math
def fibonacci_list(n):
    if n <= 0:
        return []
    fib_list = [0, 1]
    if n == 1:
        return [0]
    
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list[:n]

def index_of_first_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci(num):
    if num < 0:
        return False

    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def fibonacci_ratios(n):
    if n < 2:
        return []
    
    ratios = []
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        if a != 0:
            ratios.append(b / a)
    
    return ratios

# Test the functions

# Test for Fibonacci List
print("Fibonacci list up to 10:")
print(fibonacci_list(10))

# Test for Index of First Exceeding Value
value = 50
print(f"The index of the first Fibonacci number exceeding {value} is: {index_of_first_exceeding(value)}")

# Test for Checking Fibonacci Numbers
test_numbers = [0, 1, 2, 3, 4, 5, 6, 13, 21, 34, 55, 89, 144, 200]
for num in test_numbers:
    print(f"{num} is a Fibonacci number: {is_fibonacci(num)}")

# Test for Ratios Between Consecutive Fibonacci Numbers
ratios = fibonacci_ratios(20)
print("Ratios between consecutive Fibonacci numbers:")
for i, ratio in enumerate(ratios):
    print(f"F({i + 2})/F({i + 1}) = {ratio:.5f}")
