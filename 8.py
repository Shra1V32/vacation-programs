sum = 0

n = int(input("Enter the number: "))

dig=0
i = 0
p = 0
for k in str(n):
    i=i+1
    if int(k)%2 and i%2 == 0:
        dig=dig+1
if dig == len(k)//2:
    for i in str(n):
        p = p+1
        if p%2 == 0:
            sum=sum+int(i)
    print(f"The number has alternate digits even & sum={sum}")
else:
    print("The number doesn't have even alternate digits")