def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list .

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    max = numbers[0]
    min = numbers[0]
    for i in numbers :
        if max < i :
            max = i

    for j in numbers:
        if min > j :
            min = j

    return max-min


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed