"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

NUMBERS_TO_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
HUNDRED_WORD = "hundred"
THOUSAND_WORD = "thousand"
MILLION_WORD = "million"
TRILLION_WORD = "trillion"


def solve():
    letter_count = 0
    for n in range(1, 1001):
        number_word = number_to_word(n)
        letter_count += len(number_word)
    return letter_count


def number_to_word(n: int) -> str:
    if n < 21:
        return NUMBERS_TO_WORDS[n]
    elif n < 100:
        ones = n % 10
        tens = (n % 100 // 10) * 10
        if ones == 0:
            return NUMBERS_TO_WORDS[tens]
        else:
            return NUMBERS_TO_WORDS[tens] + NUMBERS_TO_WORDS[ones]
    elif n < 1000:
        hundreds = n % 1000 // 100
        tens = n % 100
        word = NUMBERS_TO_WORDS[hundreds] + HUNDRED_WORD
        if tens != 0:
            word += "and" + number_to_word(tens)
        return word
    elif n < 1000000:
        thousands = n % 1000000 // 1000
        word = number_to_word(thousands) + THOUSAND_WORD
        hundreds = n % 1000
        if hundreds != 0:
            word += "and" + number_to_word(hundreds)
        return word
    else:
        raise ValueError("n >= 1000000 not supported yet.")


if __name__ == "__main__":
    print(solve())
