
rev_num = 0

Base_pos = 1

def reversDigits(num):
    global rev_num
    global Base_pos
    if(num>0):
        reversDigits((int)(num/ 10))
        rev_num + = (num % 10) * Base_pos
        Base_pos *=10

    return rev_num


    num = 12993

    print("Reverse of no. is ", reversDigits(num))