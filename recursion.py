def sum(no):
    if (no == 1):
        return 1
    else:
        return (no + sum(no-1))

def start():
    n = input("Enter the last number: ")
    n = int(n)
    total = sum(n)
    print("The sum of the series from 1 to", n, "is", total)

start()