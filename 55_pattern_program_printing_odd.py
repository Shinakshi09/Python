"""

Write a program to print odd number of stars in the column

"""

number = int(input(" Please enter the number of rows you want : "))

k = 1

for i in range(1, number +1):
    for j in range(1, k+1):
        print("*", end = " ")
    k= k+2
    print()


"""

Output :

* 
* * *
* * * * *

"""

