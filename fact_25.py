# Factorial

def fact(num):
    if num>0:
        return (num*fact(num-1))
    else:
        return 1

if '__main__' == __name__:
    print(fact(int(input())))