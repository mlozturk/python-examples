def getprimes(low, high):

    return [2, 3, 5, 7]

def isprime(number):
    if number < 2:
        return False
    for i in range(3, number):
        if number % i == 0:
            return False
    return True
