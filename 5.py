num = int(input("Enter the number of elements: "))
sum=0

l=[]

for i in range(0,num):
    k = int(input(f"enter your number {i}: "))
    l.append(str(k))

for i in l:
    sum= sum+int(i[-1])
    
print(f"The sum of the last digit of the given numbers is: {sum}")
