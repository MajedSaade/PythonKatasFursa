import unittest

def sum_of_digits(input_str):
    """
    Calculates the sum of all digits in the given string.
    """
    total = 0
    for char in input_str:
        if char.isdigit():
            total += int(char)
    return total

class TestSumOfDigits(unittest.TestCase):
    def test_with_digits_and_letters(self):
        self.assertEqual(sum_of_digits("abc123"), 6)

    def test_with_spaces_and_words(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_with_no_digits(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_only_digits(self):
        self.assertEqual(sum_of_digits("9876543210"), 45)

    def test_special_characters(self):
        self.assertEqual(sum_of_digits("!2@3#4$"), 9)

if __name__ == '__main__':
    unittest.main()
