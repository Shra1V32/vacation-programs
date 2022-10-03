def isPrime(num):
    fact = 0
    for i in range(2, num):
        if num % i == 0:
            fact = fact+1
    if fact == 0:
        #print("The given number is prime number")
        return True
    else:
        #print("The given number is not a prime number")
        return False


a, b = int(input()), int(input())
if isPrime(a) and isPrime(b):
    print("Yes")
else:
    print("no")
