

"""
Printing lines with a user defined function
""" 

def print_line(n)
    """Print line with 10 characters."""
    for i in range(n):
        print("-", end="")

    # By default a \n is included at the end of the line
    print()


def main():
    """Print lines."""
    print_line(10)
    print_line(20)
    print_line(30)


main()