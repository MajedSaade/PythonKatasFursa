import unittest
from katas.sliding_window_maximum import max_sliding_window  # Replace with actual filename


class TestMaxSlidingWindow(unittest.TestCase):

    def test_example_case(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_window_size_two(self):
        nums = [9, 11, 3, 4, 8, 7]
        k = 2
        expected = [11, 11, 4, 8, 8]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_window_size_one(self):
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_entire_array_window(self):
        nums = [4, 2, 12, 3, 9]
        k = 5
        expected = [12]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_k_zero(self):
        self.assertEqual(max_sliding_window([1, 2, 3], 0), [])

    def test_k_greater_than_length(self):
        self.assertEqual(max_sliding_window([2, 1], 5), [])

    def test_empty_array(self):
        self.assertEqual(max_sliding_window([], 3), [])

    def test_all_same_elements(self):
        self.assertEqual(max_sliding_window([5, 5, 5, 5], 2), [5, 5, 5])

    def test_decreasing_elements(self):
        self.assertEqual(max_sliding_window([9, 8, 7, 6, 5], 3), [9, 8, 7])

    def test_increasing_elements(self):
        self.assertEqual(max_sliding_window([1, 2, 3, 4, 5], 3), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()
