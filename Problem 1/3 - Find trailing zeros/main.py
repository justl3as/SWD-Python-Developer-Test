def find_trailing_zeros(number: int) -> int:
    """Counts the number of trailing zeros in the factorial.

    Args:
        number: The integer to check.

    Returns:
        The number of trailing zeros.
    """

    count_zeros = 0

    # Loop as long as n is divisible by 5 (factor of 10)
    while number >= 5:
        number //= 5

        # Every division by 5 adds one trailing zero
        count_zeros += number

    return count_zeros


if __name__ == "__main__":
    input = 10
    print(find_trailing_zeros(input))
