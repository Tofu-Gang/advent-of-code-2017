__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 1: Inverse Captcha ---

You're standing in a room with "digitization quarantine" written in LEDs along 
one wall. The only door is locked, but it includes a small interface. 
"Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove 
you're not a human. Apparently, you only get one millisecond to solve the 
captcha: too fast for a normal human, but it feels like hours to you.
"""

from src.utils.utils import print_puzzle_solution


################################################################################

INPUT_FILE_PATH = "src/day_01/input.txt"

################################################################################

def get_captcha(sequence: str, step: int) -> int:
    """
    Captcha is computed as a sum of numbers that are the same as their
    step-distance neighbor to the right. step=1 means direct neighbor for puzzle
    1. For puzzle 2, step is half the original sequence size.

    :param sequence: input sequence
    :param step: distance between compared numbers
    :return: captcha from the input sequence
    """

    original_len = len(sequence)
    # The sequence is circular, so the digit after the last digit is the first
    # digit in the sequence and so on; extend the sequence to ensure this
    # behavior
    sequence += sequence[:step]
    return sum([
        int(sequence[i])
        for i in range(original_len)
        if sequence[i] == sequence[i + step]])

################################################################################

def puzzle_01() -> None:
    """
    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list. The
    list is circular, so the digit after the last digit is the first digit in
    the list.

    For example:
    -1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
     second digit and the third digit (2) matches the fourth digit.
    -1111 produces 4 because each digit (all 1) matches the next.
    -1234 produces 0 because no digit matches the next.
    -91212129 produces 9 because the only digit that matches the next one is the
     last digit, 9.

    What is the solution to your captcha?

    :return: None; Answer should be 1216.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        sequence = f.read()
        captcha = str(get_captcha(sequence, 1))
        print_puzzle_solution(captcha)


################################################################################

def puzzle_02() -> None:
    """
    You notice a progress bar that jumps to 50% completion. Apparently, the door
    isn't yet satisfied, but it did emit a star as encouragement. The
    instructions change:

    Now, instead of considering the next digit, it wants you to consider the
    digit halfway around the circular list. That is, if your list contains 10
    items, only include a digit in your sum if the digit 10/2 = 5 steps forward
    matches it. Fortunately, your list has an even number of elements.

    For example:
    -1212 produces 6: the list contains 4 items, and all four digits match the
     digit 2 items ahead.
    -1221 produces 0, because every comparison is between a 1 and a 2.
    -123425 produces 4, because both 2s match each other, but no other digit has
     a match.
    -123123 produces 12.
    -12131415 produces 4.

    What is the solution to your new captcha?

    :return: None; Answer should be 1072.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        sequence = f.read()
        captcha = str(get_captcha(sequence, int(len(sequence) / 2)))
        print_puzzle_solution(captcha)

################################################################################