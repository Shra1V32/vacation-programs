# Magic Number
# Supposing I have a number, 189, 1+8+9 = 18
# Doing this recursively, we get, 1+8 = 9, We didn't get 1 as result here
# So it isn't a magic number
# If we have a 2 digit number,
# Then we count the sum of its digits only once
# Similarily for 3,4,5... digits
# Therefore, (n-1) times

def isMagicNumber(num):
    num = str(num)
    # len(num) here is used for how many times the sum of the digits must be calculated recursively
    for i in range(0, len(num)):
        # We must initialize sum as zero
        # Else the same value of sum will be used recursively
        # We don't want that
        sum = 0
        for j in num:
            sum = sum+int(j)
        # Set num as sum, As we're going to recursively find the sum of the digits of the number
        num = str(sum)
    if sum != 1:
        print("Not a Magic number")
    else:
        print("A Magic number")

def another(num):
    num = str(num)
    req = num
    while int(req)>10:
        sum = 0
        for j in str(req):
            sum = sum+int(j)
        req = sum
    if int(req) == 10 or 1:
        return 1
    else:
        return req


print(another(int(input())))