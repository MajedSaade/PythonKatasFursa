def is_unique(string):
        for char in string:
            if string.count(char) > 1:
                return False

        return True


if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"

    print(f'"{test1}" has all unique characters: {is_unique(test1)}')  # Should be False (has repeated 'l')
    print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be True