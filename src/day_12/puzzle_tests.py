__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_12.groups import Groups


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        For example, suppose you go door-to-door like a travelling salesman and
        record the following list:
        -0 <-> 2
        -1 <-> 1
        -2 <-> 0, 3, 4
        -3 <-> 2, 4
        -4 <-> 2, 3, 6
        -5 <-> 6
        -6 <-> 4, 5

        In this example, the following programs are in the group that contains
        program ID 0:
        -Program 0 by definition.
        -Program 2, directly connected to program 0.
        -Program 3 via program 2.
        -Program 4 via program 2.
        -Program 5 via programs 6, then 4, then 2.
        -Program 6 via programs 4, then 2.

        Therefore, a total of 6 programs are in this group; all but program 1,
        which has a pipe that connects it to itself.
        """

        lines = (
            "0 <-> 2\n"
            "1 <-> 1\n"
            "2 <-> 0, 3, 4\n"
            "3 <-> 2, 4\n"
            "4 <-> 2, 3, 6\n"
            "5 <-> 6\n"
            "6 <-> 4, 5").split("\n")
        groups = Groups(lines)
        self.assertEqual(groups.get_group_size("0"), 6)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, suppose you go door-to-door like a travelling salesman and
        record the following list:
        -0 <-> 2
        -1 <-> 1
        -2 <-> 0, 3, 4
        -3 <-> 2, 4
        -4 <-> 2, 3, 6
        -5 <-> 6
        -6 <-> 4, 5

        In the example above, there were 2 groups: one consisting of programs
        0,2,3,4,5,6, and the other consisting solely of program 1.
        """

        lines = (
            "0 <-> 2\n"
            "1 <-> 1\n"
            "2 <-> 0, 3, 4\n"
            "3 <-> 2, 4\n"
            "4 <-> 2, 3, 6\n"
            "5 <-> 6\n"
            "6 <-> 4, 5").split("\n")
        groups = Groups(lines)
        self.assertEqual(groups.groups_count, 2)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
