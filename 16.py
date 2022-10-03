# 1 2 3 4 5
# 1^2 + 2^3

def sum_of_power_of_digits(n):
    n = str(n)
    sum = -1
    req = 0
    for i in n:
        sum = sum+1
        if sum+1 !=len(n):
            req = req+int(i)**int(n[sum+1])
        else:
            req = req+1
    return req


print(sum_of_power_of_digits(12345))
