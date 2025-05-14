import json
from typing import Any


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """
    result = {}

    for path in json_paths:
        try:
            with open(path, 'r') as file:
                config = json.load(file)

            result = deep_merge(result, config)
        except FileNotFoundError:
            print(f"Warning: File {path} not found. Skipping.")
        except json.JSONDecodeError:
            print(f"Warning: File {path} contains invalid JSON. Skipping.")

    return result


def deep_merge(dict1: dict, dict2: dict) -> dict:
    """
    Recursively merge two dictionaries.

    If both dictionaries have the same key and both values are dictionaries,
    the values are merged recursively. Otherwise, the value from dict2 overrides
    the value from dict1.

    Args:
        dict1: First dictionary (base)
        dict2: Second dictionary (overrides dict1)

    Returns:
        dict: The merged dictionary
    """
    result = dict1.copy()  # Create a copy to avoid modifying the original

    for key, value in dict2.items():
        # If both values are dictionaries, merge them recursively
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            # Otherwise, the value from dict2 overrides the value from dict1
            result[key] = value

    return result


if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('default.json', 'production.json', 'us-east-1-production.json')
    print(config)