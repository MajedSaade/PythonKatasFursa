import unittest
import time

from katas.time_me import measure_execution_time, sample_function, quick_function
# Replace 'your_module_name' with the actual Python file name (without .py)

class TestMeasureExecutionTime(unittest.TestCase):
    def test_sample_function_time(self):
        """Test that sample_function takes around 500 ms"""
        elapsed_time = measure_execution_time(sample_function)
        self.assertGreaterEqual(elapsed_time, 450)
        self.assertLessEqual(elapsed_time, 550)

    def test_quick_function_time(self):
        """Test that quick_function takes less than 10 ms"""
        elapsed_time = measure_execution_time(quick_function)
        self.assertLess(elapsed_time, 10)

if __name__ == '__main__':
    unittest.main()
