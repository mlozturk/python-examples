import math

class DigitInfo:
    def __init__(self, integer):
        self.integer = integer
    
    def digits(self):
        digitlist = []
        for i in reversed(range(0, len(str(self.integer)))):
            digit = self.integer // 10**i % 10
            digitlist.append(digit)
        return digitlist

    def sum(self):
        sum = 0
        for i in DigitInfo.digits(self):
            sum = sum + i
        return sum

    def sum_of_squares(self):
        sumofsquares = 0
        for i in DigitInfo.digits(self):
            sumofsquares = sumofsquares + i**2
        return sumofsquares

    def square_of_sum(self):
        return DigitInfo.sum(self)**2

    def ispalindrome(self):
        reverselist = []
        for i in range(0, len(str(self.integer))):
            digit = self.integer // 10**i % 10
            reverselist.append(digit)
        if DigitInfo.digits(self) == reverselist:
            return True
        else:
            return False
        
    def isarmstrong(self):
        armstrong = 0
        for i in DigitInfo.digits(self):
            armstrong = armstrong + i**(len(str(self.integer)))
        if armstrong == self.integer:
            return True
        else:
            return False
        