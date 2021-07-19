""" 

Perfect number : Is a positive integer that is equal to  the sum of its positive divisor excluding the number itself

6 = 1 +2 + 3 = 6

Or

Equal to the half of the sum of its all positive divisors

for example : 6 = 1, 2, 3 
= 1 + 2 + 3 + 6 = 12/2 = 6 

"""


num = int(input(" Please enter the number here : "))

result = 0

"""Positive divisor """

for i in range(1, num):
    if (num %i) ==0:
        result = result + i

if result ==num :
    print(num, "Is perfect number")

else :

    print(num, "Is not a perfect number")

    """

    Output :
    Example for number 6 

     Please enter the number here : 6
(6, 'Is perfect number')
    """

