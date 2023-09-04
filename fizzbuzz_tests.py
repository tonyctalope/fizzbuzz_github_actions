import unittest


def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(6), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(20), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
        self.assertEqual(fizzBuzz(45), "FizzBuzz")

    def test_neither(self):
        self.assertEqual(fizzBuzz(1), "1")
        self.assertEqual(fizzBuzz(2), "2")
        self.assertEqual(fizzBuzz(4), "4")


if __name__ == "__main__":
    unittest.main()
