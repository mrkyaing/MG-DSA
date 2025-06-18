def fib(n):
    if n <= 0:
        return 0 # base case for n = 0 : fib(0) = 0
    elif n == 1:
        return 1 # base case for n = 1 : fib(1) = 1
    else:
        return fib(n - 1) + fib(n - 2) # recursive case for n > 1  : fib(n) = fib(n-1) + fib(n-2) for n > 1

def print_fibonacci_series(i, n):
    if i > n:
        return
    print(fib(i), end=' ')
    print_fibonacci_series(i + 1, n)

def main():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        print(f"Fibonacci series up to {n}:")
        print_fibonacci_series(0, n)
main()
