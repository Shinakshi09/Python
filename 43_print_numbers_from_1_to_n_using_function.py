
"""
Printing natural number from 1 to n using a user defined function

"""


num=int(input("Please enter maxinmum number: "))
print("Natural numbers 1 to ",num )
def naturalNum(num):
   for i in range(1,num+1):
     print i,
naturalNum(num)