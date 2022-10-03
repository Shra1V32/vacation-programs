def isPrime(num):
    fact = 0
    for i in range(2,num):
        if num%i == 0:
            fact = fact+1
    if fact == 0:
        print("The given number is prime number")
    else:
        print("The given number is not a prime number")

isPrime(int(input()))