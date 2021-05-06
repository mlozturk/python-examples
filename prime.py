import math

def getprimes(low, high):
    primes = []
    for number in range(low, high + 1):
        if isprime(number):
            primes.append(number)
    return primes

def isprime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True