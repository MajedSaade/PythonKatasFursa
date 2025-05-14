from typing import List


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """
    all_requirements = set()
    for test_case in test_cases:
        all_requirements.update(test_case)

    selected_indices = []
    covered_requirements = set()

    while covered_requirements != all_requirements:
        best_index = -1
        best_coverage = 0

        for i, test_case in enumerate(test_cases):
            if i in selected_indices:
                continue

            new_coverage = len(set(test_case) - covered_requirements)

            if new_coverage > best_coverage:
                best_coverage = new_coverage
                best_index = i

        if best_index != -1:
            selected_indices.append(best_index)
            covered_requirements.update(test_cases[best_index])

    return selected_indices


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]