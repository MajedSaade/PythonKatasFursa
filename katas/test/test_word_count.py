import unittest
from katas.word_count import count_words

class TestCountWords(unittest.TestCase):

    def test_normal_sentence(self):
        """Test a normal sentence with spaces"""
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_single_word(self):
        """Test a sentence with a single word"""
        self.assertEqual(count_words("Hello"), 1)

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(count_words(""), 0)

    def test_multiple_spaces(self):
        """Test a sentence with multiple spaces between words"""
        self.assertEqual(count_words("This    has   multiple     spaces"), 4)

    def test_leading_and_trailing_spaces(self):
        """Test a sentence with spaces at the start and end"""
        self.assertEqual(count_words("   Leading and trailing spaces   "), 4)

    def test_only_spaces(self):
        """Test a string that contains only spaces"""
        self.assertEqual(count_words("        "), 0)


if __name__ == '__main__':
    unittest.main()
