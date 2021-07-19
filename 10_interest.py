"""     Interest formula    """
# P = Principal
# T = Time / Duration / Years
# R =  rate of interest


print("______Simple Interest report_____")

#name = input(" Please enter your name here : ")

p = float(input(" Enter the principles"))

t = int(input(" Please enter the number of years"))

r = float(input("Enter  the rate of interest"))

simple_interest = p*t*r / 100

print("Your simple interest is" + " "  + str(simple_interest))

