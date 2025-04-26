import unittest


def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")

    def test_edge_cases(self):
        self.assertEqual(longest_common_prefix([""]), "")
        self.assertEqual(longest_common_prefix(["a"]), "a")
        self.assertEqual(longest_common_prefix(["abc", "abc", "abc"]), "abc")
        self.assertEqual(longest_common_prefix(["prefix", "pre"]), "pre")
        self.assertEqual(longest_common_prefix(["different", "words"]), "")


if __name__ == '__main__':
    unittest.main()
