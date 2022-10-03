def cyclic_add(n):
    n = str(n)
    count = -1
    sum = 0
    for i in n:
        count = count+1
        sum = sum+int(n[count:])
    return sum


print(cyclic_add(123))

# 123 + 23 + 3
