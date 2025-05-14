import unittest
from katas.max_storage_capacity import max_storage_area  # Replace with your actual filename

class TestMaxStorageArea(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_empty_list(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_single_element(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_all_same_height(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)

    def test_strictly_increasing(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # 3x3 from indices 2-4

    def test_strictly_decreasing(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # 3x3 from indices 0-2

    def test_peak_in_middle(self):
        self.assertEqual(max_storage_area([2, 4, 6, 4, 2]), 12)

    def test_plateau(self):
        self.assertEqual(max_storage_area([1, 2, 5, 5, 5, 2, 1]), 15)  # 5x3 plateau

    def test_two_elements(self):
        self.assertEqual(max_storage_area([2, 1]), 2)

if __name__ == '__main__':
    unittest.main()
