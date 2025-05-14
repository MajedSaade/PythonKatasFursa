import unittest
from katas.semantic_version_comparator import compare_versions  # Replace with actual filename

class TestCompareVersions(unittest.TestCase):

    def test_equal_versions(self):
        self.assertEqual(compare_versions("1.2.3", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.2", "1.2.0"), 0)
        self.assertEqual(compare_versions("1", "1.0.0"), 0)

    def test_less_than(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("1.2.0", "1.2.1"), -1)
        self.assertEqual(compare_versions("1.9.9", "2.0.0"), -1)
        self.assertEqual(compare_versions("1.2", "1.2.1"), -1)

    def test_greater_than(self):
        self.assertEqual(compare_versions("2.1.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.10.0", "1.2.0"), 1)
        self.assertEqual(compare_versions("1.2.3", "1.2.2"), 1)
        self.assertEqual(compare_versions("1.2.1", "1.2"), 1)

    def test_padding_behavior(self):
        self.assertEqual(compare_versions("1.0", "1.0.0.0.0"), 0)
        self.assertEqual(compare_versions("1.0.0.1", "1.0"), 1)
        self.assertEqual(compare_versions("1.0.0.0", "1.0.1"), -1)

    def test_multi_digit_components(self):
        self.assertEqual(compare_versions("1.10.0", "1.2.9"), 1)
        self.assertEqual(compare_versions("1.0.20", "1.0.3"), 1)

if __name__ == '__main__':
    unittest.main()
