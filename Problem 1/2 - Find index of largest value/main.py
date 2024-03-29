from ast import List


def find_index_largest_value(numbers: List) -> int:
    """Finds the index of the largest value in a list.

    Args:
        nums: The list to search.

    Returns:
        The index of the largest value in the list.
    """

    if not numbers:
        return 0

    max_value = numbers[0]
    max_index = 0

    for i, value in enumerate(numbers):
        if value >= max_value:
            max_value = value
            max_index = i

    return max_index


if __name__ == "__main__":
    input = [1, 2, 1, 3, 5, 6, 4]
    print(find_index_largest_value(input))  # out 5
