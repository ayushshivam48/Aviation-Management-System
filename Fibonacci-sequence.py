def fibonacci_recursive(n):
    """Compute Fibonacci number using a naive recursive approach."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n, memo={}):
    """Compute Fibonacci number using memoization to optimize recursion."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_tabulation(n):
    """Compute Fibonacci number using tabulation (bottom-up approach)."""
    if n <= 1:
        return n
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value for different Fibonacci numbers

    print(f"Fibonacci of {n} using recursion: {fibonacci_recursive(n)}")
    print(f"Fibonacci of {n} using memoization: {fibonacci_memoization(n)}")
    print(f"Fibonacci of {n} using tabulation: {fibonacci_tabulation(n)}")
