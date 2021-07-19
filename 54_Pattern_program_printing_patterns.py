""" Pattern program - Printing stars * in right angel triangel shape """

number = int(input(" Please enter the number of rows you want : "))

for i in range(0, number+ 1):
    for j in range(1, i+1):
        print("*", end= " ")
    print()



""" 

Output :

*
* *
* * *
* * * *
* * * * *


"""