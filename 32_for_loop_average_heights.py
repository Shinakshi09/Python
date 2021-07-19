'''

You are going to write a program that calculates the average student height from a List of heights.

'''

army_men_heights = input(" Input the list of the Army mens heights ").split()

for n in range(0, len(army_men_heights)):
    army_men_heights[n] = int(army_men_heights[n])

print(army_men_heights)
