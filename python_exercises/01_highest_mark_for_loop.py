
"""

Write a program which calculates  the highest marks from a list of marks

student_marks= [90, 100, 80, 94, 85, 65]


Note : You are not allowed to use min or max functions. Output must be "The highest mark in the class is : x"

"""

student_marks = input("Input a list of student scores ").split()
for n in range(0, len(student_marks)):
  student_marks[n] = int(student_marks[n])
print(student_marks)


highest_mark = 0

for mark in student_marks:

  if mark > highest_mark:
    highest_mark = mark


print(f"The highest score in the class is: {highest_mark}")
