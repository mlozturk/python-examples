import unittest
import prime

class TestPrime(unittest.TestCase):

    def test_isprime(self):
        self.assertFalse(prime.isprime(8))
        self.assertTrue(prime.isprime(2))
        self.assertFalse(prime.isprime(9))
        self.assertTrue(prime.isprime(17))
        self.assertFalse(prime.isprime(-1))
        self.assertFalse(prime.isprime(-8))
        self.assertFalse(prime.isprime(4))

    def test_getprimes(self):
        self.assertEqual(prime.getprimes(-10, 10), [2, 3, 5, 7])
        self.assertEqual(prime.getprimes(-10, 1), [])
        self.assertEqual(prime.getprimes(-10, 2), [2])
        self.assertEqual(prime.getprimes(100, 103), [101, 103])

if __name__ == '__main__':
    unittest.main()