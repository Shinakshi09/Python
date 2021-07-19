""" Bubble sorting algorithm """


List = [50, 32, 52, 0]

for j in range(len(List)-1):
    for i in range(len(List)-1):
        if  List[i] > List[i+1]:
            List[i], List[i + 1] = List[i+1], List[i]


print("Sorted List", List)

"""

Output :

('Sorted List', [0, 32, 50, 52])

"""

