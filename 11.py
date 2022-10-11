def unique_digits(n):
    n = str(n)
    k = []
    for i in n:
        if n.count(i) != 1:
            print("Non-Unique Number")
            break
        else:
            k.append(i)
            #continue
    if "".join(k) == n:
        print("Unique Number")
unique_digits(123)