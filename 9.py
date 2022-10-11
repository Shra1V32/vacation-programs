sum=0
c=[]
n = int(input("Enter the number: "))

for i in str(n):
    c.append(i)
    sum=sum+int(i)

print(f"The sum of all the digits {sum}, Number of digits={len(c)}")
