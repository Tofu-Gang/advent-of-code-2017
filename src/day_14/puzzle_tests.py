__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_14.disk import Disk


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        For example, if your key string were flqrgnkx, 8108 squares are used
        across the entire 128x128 grid.
        """

        self.assertEqual(Disk("flqrgnkx").used_count, 8108)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, if your key string were flqrgnkx, 1242 regions are present.
        """

        self.assertEqual(Disk("flqrgnkx").groups_count, 1242)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
