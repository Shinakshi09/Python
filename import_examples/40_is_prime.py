""" Is prime """


def is_prime(n):
    """ It is a prime number


    -----

    Args :

    num : An integer 

    Returns 

    Boolean (Prime or not)

    """


if num == 0  or num ==1:
    return  "It is an invalid number"
if num ==2:
    return True

for  i in range (2, n):
    if num % i == 0:

        return false

    return True

if __name__ == "__main__":
    print("25", is_prime(25))
    print("919", is_prime(919))