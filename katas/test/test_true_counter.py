import unittest
from katas.true_counter import count_true_values
# Replace 'your_module_name' with the actual Python file name (without .py)

class TestCountTrueValues(unittest.TestCase):

    def test_mixed_values(self):
        """Test list with both True and False values"""
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_all_true(self):
        """Test list where all values are True"""
        self.assertEqual(count_true_values([True, True, True]), 3)

    def test_all_false(self):
        """Test list where all values are False"""
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(count_true_values([]), 0)

    def test_single_true(self):
        """Test a list with a single True value"""
        self.assertEqual(count_true_values([True]), 1)

    def test_single_false(self):
        """Test a list with a single False value"""
        self.assertEqual(count_true_values([False]), 0)


if __name__ == '__main__':
    unittest.main()
