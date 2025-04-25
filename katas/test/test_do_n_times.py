import unittest
from contextlib import redirect_stdout
from io import StringIO

from katas.do_n_times import do_n_times, say_hello, print_message

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        expected = """Calling function 3 times:
Hello!
Hello!
Hello!
Calling another function 5 times:
Python is fun!
Python is fun!
Python is fun!
Python is fun!
Python is fun!
"""

        f = StringIO()
        with redirect_stdout(f):
            print("Calling function 3 times:")
            do_n_times(say_hello, 3)
            print("Calling another function 5 times:")
            do_n_times(print_message, 5)

        self.assertEqual(f.getvalue(), expected)