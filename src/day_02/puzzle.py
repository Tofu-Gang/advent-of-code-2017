__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. 
"You there! Your state appears to be idle. Come help us repair the corruption in 
this spreadsheet - if we take another millisecond, we'll have to display an 
hourglass cursor!"
"""

from typing import List
from itertools import combinations
from src.utils.utils import print_puzzle_solution


################################################################################

INPUT_FILE_PATH = "src/day_02/input.txt"

################################################################################

def _parse_spreadsheet(spreadsheet: str) -> List[List[int]]:
    """
    :param spreadsheet: input spreadsheet as a string
    :return: parsed spreadsheet as a list of lists of numbers
    """

    return [[int(number) for number in row.split()]
            for row in spreadsheet.split("\n")]

################################################################################

def get_checksum(spreadsheet: str) -> int:
    """
    For each row, determine the difference between the largest value and the
    smallest value; the checksum is the sum of all of these differences.

    :param spreadsheet: input spreadsheet
    :return: puzzle 1 checksum
    """

    rows = _parse_spreadsheet(spreadsheet)
    return sum(max(row) - min(row) for row in rows)

################################################################################

def get_evenly_divisible_checksum(spreadsheet: str) -> int:
    """
    For each row, find the only two numbers where one evenly divides the other.
    Divide those numbers and add up each line's result.

    :param spreadsheet: input spreadsheet
    :return: puzzle 2 checksum
    """

    rows = _parse_spreadsheet(spreadsheet)
    return sum(
        int(max(combination) / min(combination))
        for row in rows
        for combination in combinations(row, 2)
        if max(combination) % min(combination) == 0)

################################################################################

def puzzle_01() -> None:
    """
    The spreadsheet consists of rows of apparently-random numbers. To make sure
    the recovery process is on the right track, they need you to calculate the
    spreadsheet's checksum. For each row, determine the difference between the
    largest value and the smallest value; the checksum is the sum of all of
    these differences.

    For example, given the following spreadsheet:
    5 1 9 5
    7 5 3
    2 4 6 8

    -The first row's largest and smallest values are 9 and 1, and their
     difference is 8.
    -The second row's largest and smallest values are 7 and 3, and their
     difference is 4.
    -The third row's difference is 6.

    In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

    What is the checksum for the spreadsheet in your puzzle input?

    :return: None; Answer should be 37923.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        spreadsheet = f.read()
        checksum = get_checksum(spreadsheet)
        print_puzzle_solution(checksum)

################################################################################

def puzzle_02() -> None:
    """
    "Great work; looks like we're on the right track after all. Here's a star
    for your effort." However, the program seems a little worried. Can programs
    be worried?

    "Based on what we're seeing, it looks like all the User wanted is some
    information about the evenly divisible values in the spreadsheet.
    Unfortunately, none of us are equipped for that kind of calculation - most
    of us specialize in bitwise operations."

    It sounds like the goal is to find the only two numbers in each row where
    one evenly divides the other - that is, where the result of the division
    operation is a whole number. They would like you to find those numbers on
    each line, divide them, and add up each line's result.

    For example, given the following spreadsheet:
    5 9 2 8
    9 4 7 3
    3 8 6 5

    -In the first row, the only two numbers that evenly divide are 8 and 2; the
     result of this division is 4.
    -In the second row, the two numbers are 9 and 3; the result is 3.
    -In the third row, the result is 2.

    In this example, the sum of the results would be 4 + 3 + 2 = 9.

    What is the sum of each row's result in your puzzle input?

    :return: None; Answer should be 263.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        spreadsheet = f.read()
        checksum = get_evenly_divisible_checksum(spreadsheet)
        print_puzzle_solution(checksum)

################################################################################
