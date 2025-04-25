import unittest


def is_unique(string):
    for char in string:
        if string.count(char) > 1:
            return False
    return True


class TestIsUnique(unittest.TestCase):

    def test_is_unique(self):
        # Test cases to validate is_unique function
        self.assertFalse(is_unique("Hello"))  # Expected: False (has repeated 'l')
        self.assertTrue(is_unique("World"))  # Expected: True (all unique)
        self.assertTrue(is_unique("Python"))  # Expected: True (all unique)
        self.assertTrue(is_unique("Unique"))  # Expected: True (all unique)


if __name__ == '__main__':
    unittest.main()
