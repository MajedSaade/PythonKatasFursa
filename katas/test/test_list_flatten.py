import unittest


def flatten_list(nested_list):
    res = []
    for i in nested_list:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res


class TestFlattenList(unittest.TestCase):

    def test_flatten_list(self):
        # Basic nested list
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7])

        # No nesting
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

        # Deep nesting
        self.assertEqual(flatten_list([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])

        # Empty list
        self.assertEqual(flatten_list([]), [])

        # Nested empty lists
        self.assertEqual(flatten_list([[], [[], []]]), [])

        # List with one nested list
        self.assertEqual(flatten_list([[1, 2, 3]]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
