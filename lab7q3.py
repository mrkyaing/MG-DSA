def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

def main():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        if is_even(n):
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")

main()