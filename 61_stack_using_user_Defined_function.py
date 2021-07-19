""" Stack using user defined function """

stack = []

def push():
    element = input("please enter the element : ")
    stack.append(element)
    print(stack)


def pop_element():
    if not stack:
        print(" Stack is empty")
    else :
        e = stack.pop()
        print("removed element : ", e)
        print(stack)

while True:
    print(" Select the operation 1. push, 2, pop, 4, quit")
    choice = int(intput())
    if choice ==1:
         