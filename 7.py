limit = 5

l=[]

for i in range(0,limit):
    k = int(input(f"Enter the {i+1} element: "))
    if k%2 == 0:
        l.append(k)

print(f"There are {len(l)} even numbers")