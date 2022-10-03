# Special Number
import fact_25
def isSpecialNumber(num):
    sum = 0
    for i in str(num):
        sum = sum+fact_25.fact(int(i))

    if num == sum:
        return True
    else:
        return False

if '__main__' == __name__:
    print(isSpecialNumber(int(input())))