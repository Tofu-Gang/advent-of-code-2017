__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from puzzle import get_checksum, get_evenly_divisible_checksum


class TestDay01(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
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
        """

        spreadsheet = "5 1 9 5\n7 5 3\n2 4 6 8"
        self.assertEqual(get_checksum(spreadsheet), 18)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, given the following spreadsheet:
        5 9 2 8
        9 4 7 3
        3 8 6 5

        -In the first row, the only two numbers that evenly divide are 8 and 2;
         the result of this division is 4.
        -In the second row, the two numbers are 9 and 3; the result is 3.
        -In the third row, the result is 2.

        In this example, the sum of the results would be 4 + 3 + 2 = 9.
        """

        spreadsheet = "5 9 2 8\n9 4 7 3\n3 8 6 5"
        self.assertEqual(get_evenly_divisible_checksum(spreadsheet), 9)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
