def convert_number_to_thai(number: int) -> str:
    """Converts a non-negative integer to its corresponding Thai word representation.

    Args:
        number: The integer to check.

    Returns:
        The Thai text representation of the number
    """

    assert 0 <= number <= 10**7

    # Handling the special case when the number is 0
    if number == 0:
        return "ศูนย์"

    # Define mappings for digits and place values in Thai
    digits_thai = {
        0: "",
        1: "หนึ่ง",
        2: "สอง",
        3: "สาม",
        4: "สี่",
        5: "ห้า",
        6: "หก",
        7: "เจ็ด",
        8: "แปด",
        9: "เก้า",
    }

    place_values_thai = {
        1: "",
        10: "สิบ",
        100: "ร้อย",
        1000: "พัน",
        10000: "หมื่น",
        100000: "แสน",
        1000000: "ล้าน",
    }

    thai_text = ""
    place_value = 1

    # Looping until the number becomes 0
    while number > 0:
        digit = number % 10
        number = number // 10

        # Handle cases for place values more than 1 million
        if place_value == 1000000:
            place_value_text = place_values_thai[place_value]
            thai_text = place_value_text + thai_text
            place_value = 1

        if digit > 0:
            digit_text = digits_thai[digit]

            # special cases for 1 and 2
            if digit == 1:
                if place_value == 1 and number != 0:  # Use "เอ็ด" instead of "หนึ่ง"
                    digit_text = "เอ็ด"
                elif place_value == 10:
                    digit_text = ""

            elif digit == 2:
                if place_value == 10:  # Use "เอ็ด" instead of "หนึ่ง"
                    digit_text = "ยี่"

            place_value_text = place_values_thai[place_value]
            thai_text = digit_text + place_value_text + thai_text

        place_value *= 10  # Update the place value for the next iteration

    return thai_text


if __name__ == "__main__":
    input = 10000000
    print(convert_number_to_thai(input))
