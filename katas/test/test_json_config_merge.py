import unittest
import tempfile
import json
import os
from typing import Any
from katas.json_config_merge import json_configs_merge, deep_merge  # Replace with your actual filename

class TestJsonConfigsMerge(unittest.TestCase):

    def create_temp_json_file(self, data: dict[str, Any]) -> str:
        """Helper function to create a temporary JSON file and return its path."""
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
        json.dump(data, temp_file)
        temp_file.close()
        return temp_file.name

    def test_simple_merge(self):
        file1 = self.create_temp_json_file({"a": 1, "b": 2})
        file2 = self.create_temp_json_file({"b": 3, "c": 4})

        merged = json_configs_merge(file1, file2)
        self.assertEqual(merged, {"a": 1, "b": 3, "c": 4})

        os.unlink(file1)
        os.unlink(file2)

    def test_nested_merge(self):
        file1 = self.create_temp_json_file({"a": {"x": 1}, "b": 2})
        file2 = self.create_temp_json_file({"a": {"y": 2}, "b": 3})

        merged = json_configs_merge(file1, file2)
        self.assertEqual(merged, {"a": {"x": 1, "y": 2}, "b": 3})

        os.unlink(file1)
        os.unlink(file2)

    def test_file_not_found(self):
        merged = json_configs_merge("nonexistent_file.json")
        self.assertEqual(merged, {})  # Should just skip and return empty dict

    def test_invalid_json(self):
        # Create a file with invalid JSON
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
        temp_file.write("{ invalid json }")
        temp_file.close()

        merged = json_configs_merge(temp_file.name)
        self.assertEqual(merged, {})

        os.unlink(temp_file.name)

class TestDeepMerge(unittest.TestCase):

    def test_flat_override(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(deep_merge(dict1, dict2), expected)

    def test_nested_override(self):
        dict1 = {"a": {"x": 1, "z": 0}, "b": 2}
        dict2 = {"a": {"y": 2}, "b": 3}
        expected = {"a": {"x": 1, "z": 0, "y": 2}, "b": 3}
        self.assertEqual(deep_merge(dict1, dict2), expected)

    def test_non_dict_override(self):
        dict1 = {"a": {"x": 1}}
        dict2 = {"a": 42}
        expected = {"a": 42}
        self.assertEqual(deep_merge(dict1, dict2), expected)

if __name__ == '__main__':
    unittest.main()
