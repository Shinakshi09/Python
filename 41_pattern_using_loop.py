"""

Print the following patterns using loop :
a.
*
**
***
****
b.
   *  
 *** 
*****
 *** 
   *  
c.
1010101
 10101 
  101  
   1   

"""

#a.

i = 1
while i<=4:
    print ("*" *i)
    i = i+1

#b.

i = 1
j = 2

while i >=1:
    a = " "*j+"*"*i+ " "*j
    print(a)
    i = i+2
    j = j-1
    if i>5:
        break

    i = 3

    j = 1

    while i>1:
        a = " " *j + "*" *i+" "*j
        print(a)
        i = i-2
        j = j+1
    

    """

    It is made infinite loop intentionally 

    """
    

