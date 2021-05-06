import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz([1, 3, 5, 15, 30, 20]),
            ['1', 'fizz', 'buzz', 'fizzbuzz', 'fizzbuzz', 'buzz'])
        self.assertEqual(fizzbuzz.fizzbuzz([]), [])
        self.assertEqual(fizzbuzz.fizzbuzz([3]), ['fizz'])
        self.assertEqual(fizzbuzz.fizzbuzz([5]), ['buzz'])
        self.assertEqual(fizzbuzz.fizzbuzz([15]), ['fizzbuzz'])
        self.assertEqual(fizzbuzz.fizzbuzz(range(14, 17)), ['14','fizzbuzz', '16'])

if __name__ == '__main__':
    unittest.main()