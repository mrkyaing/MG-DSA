def sum(n):
    if (n == 1):
        return 1 #base case
    else:
        return (n + sum(n-1)) # recursive case
def main():
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        result = sum(n)
        print(f"The sum of from 1 to {n} natural numbers is: {result}")

main()