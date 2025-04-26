import unittest
from copy import deepcopy
from katas.matrix_rotate import rotate_matrix

# Assuming rotate_matrix is imported or defined above this test class
# If it's in another file, you can import it like:
# from your_module_name import rotate_matrix

class TestRotateMatrix(unittest.TestCase):
    def test_rotate_3x3_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        matrix_copy = deepcopy(matrix)
        rotate_matrix(matrix_copy)
        self.assertEqual(matrix_copy, expected)

    def test_rotate_2x2_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expected = [
            [3, 1],
            [4, 2]
        ]
        matrix_copy = deepcopy(matrix)
        rotate_matrix(matrix_copy)
        self.assertEqual(matrix_copy, expected)

    def test_rotate_1x1_matrix(self):
        matrix = [
            [1]
        ]
        expected = [
            [1]
        ]
        matrix_copy = deepcopy(matrix)
        rotate_matrix(matrix_copy)
        self.assertEqual(matrix_copy, expected)

    def test_rotate_4x4_matrix(self):
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        matrix_copy = deepcopy(matrix)
        rotate_matrix(matrix_copy)
        self.assertEqual(matrix_copy, expected)

if __name__ == '__main__':
    unittest.main()
