"""
Cube sum of  first  n natural numbers
"""


def sum_of_series(n):
    sum = 0
    for i in range (1, n+1):
        sum +=i*i*i

        return sum

n= 10

sum_of_series(10)