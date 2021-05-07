import unittest
import digitinfo

class TestDigitInfo(unittest.TestCase):
    def test_digits(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.digits(), [1, 7, 9, 8])
    
    def test_sum(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.sum(), 25)

    def test_sum_of_squares(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.sum_of_squares(), 195)

    def test_square_of_sum(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.square_of_sum(), 625)

    def test_ispalindrome(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.ispalindrome(), False)
        info = digitinfo.DigitInfo(121)
        self.assertEqual(info.ispalindrome(), True)

    def test_isarmstrong(self):
        info = digitinfo.DigitInfo(1798)
        self.assertEqual(info.isarmstrong(), False)    
        info = digitinfo.DigitInfo(370)
        self.assertEqual(info.isarmstrong(), True)    

if __name__ == '__main__':
    unittest.main()