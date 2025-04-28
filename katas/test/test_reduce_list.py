import unittest

def reduce_array(numbers):
    """
    Modifies the list so that each element becomes the difference between
    itself and its predecessor. The first element remains unchanged.
    """
    length = len(numbers)
    for i in range(length - 1, 0, -1):
        numbers[i] = numbers[i] - numbers[i - 1]

def print_list(array):
    """
    Helper function to print the elements of a list.
    """
    print(' '.join(str(num) for num in array))


class TestReduceArray(unittest.TestCase):
    def test_example_case(self):
        numbers = [10, 15, 7, 20, 25]
        expected = [10, 5, -8, 13, 5]
        reduce_array(numbers)
        self.assertEqual(numbers, expected)

    def test_single_element(self):
        numbers = [5]
        expected = [5]  # Single element should stay the same
        reduce_array(numbers)
        self.assertEqual(numbers, expected)

    def test_empty_list(self):
        numbers = []
        expected = []
        reduce_array(numbers)
        self.assertEqual(numbers, expected)

    def test_two_elements(self):
        numbers = [7, 10]
        expected = [7, 3]  # 10 - 7 = 3
        reduce_array(numbers)
        self.assertEqual(numbers, expected)

if __name__ == '__main__':
    unittest.main()
