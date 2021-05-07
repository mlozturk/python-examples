import math

class DigitInfo:
    def __init__(self, integer):
        self._integer = integer
        self._digits = []
        while integer > 0:
            self._digits.append(integer % 10)
            integer //= 10
        self._digits.reverse()
    
    def digits(self):
        return self._digits

    def sum(self):
        return sum(self._digits)

    def sum_of_squares(self):
        return sum([i * i for i in self._digits])
        # return sum(map(lambda i : i * i, self._digits))

    def square_of_sum(self):
        return self.sum()**2

    def ispalindrome(self):
        return self._digits == list(reversed(self._digits))
        
    def isarmstrong(self):
        return sum(map(lambda i : i ** len(self._digits),
            self._digits)) == self._integer