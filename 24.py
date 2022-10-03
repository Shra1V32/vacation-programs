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

def isTwistedPrime(num):
    if isPrime(num) and isPrime(int(str(num)[::-1])):
        return True
    else:
        return False

print(isTwistedPrime(int(input())))