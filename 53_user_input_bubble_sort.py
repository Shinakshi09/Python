""" Bubble sort algorithm using a user input list """

list1 = [] 
  
n = int(input("Enter number of elements : ")) 
  
for k in range(0, n): 
    ele = int(input()) 
  
    list1.append(ele)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if  list1[i] > list1[i+1]:
            list1[i], list1[i + 1] = list1[i+1], list1[i]


print("Sorted List", list1)