import unittest
from katas.is_valid_git_tree import is_valid_git_tree  # Replace with actual filename or comment out if testing in same file

class TestIsValidGitTree(unittest.TestCase):

    def test_valid_tree(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_cycle_in_tree(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]  # Cycle
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_multiple_roots(self):
        tree = {
            "A": ["B"],
            "C": ["D"]
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_disconnected_nodes(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": []  # Disconnected node
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_single_node(self):
        tree = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_empty_tree(self):
        tree = {}
        self.assertFalse(is_valid_git_tree(tree))  # No nodes, so no root

if __name__ == '__main__':
    unittest.main()
