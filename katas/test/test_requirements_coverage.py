import unittest
from katas.requirements_coverage import select_minimal_test_cases  # Replace with actual filename

class TestSelectMinimalTestCases(unittest.TestCase):

    def test_example_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set(result) in [{2, 3}, {0, 1, 3}, {0, 2, 3}, {2, 4, 1}])  # Multiple valid minimal covers

    def test_single_test_case(self):
        test_cases = [[1, 2, 3]]
        self.assertEqual(select_minimal_test_cases(test_cases), [0])

    def test_fully_overlapping_cases(self):
        test_cases = [
            [1, 2],
            [1, 2],
            [1, 2]
        ]
        self.assertEqual(select_minimal_test_cases(test_cases), [0])  # Any one of them is sufficient

    def test_disjoint_requirements(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertCountEqual(result, [0, 1, 2, 3])  # All needed to cover all requirements

    def test_efficiency_on_order(self):
        test_cases = [
            [1],
            [1, 2],
            [2, 3],
            [3, 4],
            [4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set(result).issubset({1, 2, 3}))  # Should skip [0] and [4]

    def test_minimum_coverage_set(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set(result) in [{0, 1}, {1, 2}, {0, 2}])  # Any two can cover 1, 2, 3

if __name__ == '__main__':
    unittest.main()
