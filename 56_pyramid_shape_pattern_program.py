"""

Pyramid shape pattern program

"""

number = int(input(" Please enter the number of rows :"))

for i in range(0, number):
    for j in range(0, number-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end = " ")
    print()



"""

Output :

    *
 * * * * 
* * * * * *

"""