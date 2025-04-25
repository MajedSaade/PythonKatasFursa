import unittest


def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list .

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    max_num = numbers[0]
    min_num = numbers[0]
    for i in numbers:
        if max_num < i:
            max_num = i

    for j in numbers:
        if min_num > j:
            min_num = j

    return max_num - min_num


class TestFindDifference(unittest.TestCase):

    def test_find_difference(self):
        # Test cases to validate find_difference function
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)  # 20 - (-2) = 22
        self.assertEqual(find_difference([1, 2, 3]), 2)  # 3 - 1 = 2
        self.assertEqual(find_difference([0, 0, 0, 0]), 0)  # All numbers are the same, so difference is 0
        self.assertEqual(find_difference([-10, -20, 30]), 50)  # 30 - (-20) = 50
        self.assertEqual(find_difference([5]), 0)  # Only one number, so difference is 0


if __name__ == '__main__':
    unittest.main()
