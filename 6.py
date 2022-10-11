num = int(input("Enter the number: "))
l=[]
num = str(num)

for i in num:
    if i == '0':
        l.append(i)

print(f"The number of zeroes in the given number is: {len(l)}")