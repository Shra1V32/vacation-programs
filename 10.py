n = int(input("Enter your number: "))

n = str(n)
z= n

for i in n:
    if n.count(i) == 1:
        print(i, "is unique")

        
