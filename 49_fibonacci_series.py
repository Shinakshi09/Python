"""  

print Fibonacci series upto n terms

Fibonacci series is a series of numbers where the current number is the sum of previous two terms. 

For Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... , (n-1th + n-2th) 

"""

def Fibonacci(n):
    a = 0
    b = 1

    if n ==1:
        print(a)

    else:

        print(a)
        print(b)

    """ Running through for loop to get further numbers"""

    for i in range(2, n):
        c = a + b
        """ Swapping the numbers """
        a = b
        b = c

        print(c)


""" calling the function """

Fibonacci(10)


"""

Output :

0
1
1
2
3
5
8
13
21
34

"""


