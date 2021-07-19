## Calculating maximum of three numbers

number1 = float(input("What is your first number  "))

number2 = float(input("What is your second number  "))

number3 = float(input("What is your third number  "))

if (number1>number2) and (number1 > number3):

    maximum_number = number1

    print("Number 1 is the maximum number")

elif (number2>number1) and (number2>number3):
    maximum_number = number2

    print("Number 2 is the maximum number")

else :

    print(" Number3 will Maximum number among 3 numbers ")


