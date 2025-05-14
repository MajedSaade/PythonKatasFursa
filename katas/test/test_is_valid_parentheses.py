import unittest
from katas.is_valid_parentheses import is_valid_parentheses  # Replace with actual filename or comment out if in same file

class TestIsValidParentheses(unittest.TestCase):

    def test_all_types_valid(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_mismatched_types(self):
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_nested_valid(self):
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_unbalanced_open(self):
        self.assertFalse(is_valid_parentheses("((("))

    def test_unbalanced_close(self):
        self.assertFalse(is_valid_parentheses(")))"))

    def test_partial_pairs(self):
        self.assertFalse(is_valid_parentheses("({[})]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_only_opening(self):
        self.assertFalse(is_valid_parentheses("[[["))

    def test_only_closing(self):
        self.assertFalse(is_valid_parentheses("]]]"))

    def test_long_valid_sequence(self):
        self.assertTrue(is_valid_parentheses("([{}({})[]])"))

if __name__ == '__main__':
    unittest.main()
