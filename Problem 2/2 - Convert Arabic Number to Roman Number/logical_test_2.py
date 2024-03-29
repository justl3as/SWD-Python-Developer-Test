def convert_number_to_roman(number: int) -> str:
    """Converts integer to Roman numeral.

    Args:
        number: The integer to check.

    Returns:
        The Roman numeral.
    """

    assert 0 <= number <= 1000

    # Dictionary mapping integer to Roman numerals
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman_string = ""

    # Iterating through the keys in the Roman numeral dictionary
    for value in roman_numerals.keys():
        while number >= value:
            number -= value
            roman_string += roman_numerals[value]

    return roman_string


if __name__ == "__main__":
    input = 443
    print(convert_number_to_roman(input))  # out CDXLIII
