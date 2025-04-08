
import sys
sys.setrecursionlimit(10000)

memo = {}

def fibonacci_3(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_3(n-1) + fibonacci_3(n-2)
    return memo[n]
