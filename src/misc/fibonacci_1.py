
def fibonacci_1(n):
    if n <= 1:
        return 1
    return fibonacci_1(n-1) + fibonacci_1(n-2)