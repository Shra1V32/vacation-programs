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

def isTwinPrime(a, b):
    if abs(a-b) == 2 and isPrime(a) and isPrime(b):
        return True
    else:
        return False

print(isTwinPrime(int(input()),int(input())))
