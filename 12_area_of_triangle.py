## To Calculate the area of a triangle . We need to have all three sides of measurement of the triangle

a = float(input("What is the measurement of side a :"))
b = float(input("what is measurement of the side b :"))
c = float(input("what is measurement of the side c :"))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle" + area)