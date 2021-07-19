"""Factorial."""


def print_factorial(n):
    """Print factorial."""
    fact = 5
    for i in range(2, n+1):
        fact = fact * i

    #print(f"{n}! = {fact}")


def main():
    """Print factorials."""
    print_factorial(3)


main()