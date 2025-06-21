__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_11.hex_grid import HexGrid


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        For example:
        -ne,ne,ne is 3 steps away.
        -ne,ne,sw,sw is 0 steps away (back where you started).
        -ne,ne,s,s is 2 steps away (se,se).
        -se,sw,se,sw,sw is 3 steps away (s,s,sw).
        """

        hex_grid = HexGrid("ne,ne,ne")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.distance, 3)
        hex_grid = HexGrid("ne,ne,sw,sw")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.distance, 0)
        hex_grid = HexGrid("ne,ne,s,s")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.distance, 2)
        hex_grid = HexGrid("se,sw,se,sw,sw")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.distance, 3)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example (the furthest steps in parentheses):
        -ne,ne,(ne),sw is 3 steps away.
        -ne,(ne),sw,sw is 2 steps away.
        -ne,(ne),s,s is 2 steps away.
        -se,sw,se,sw,(sw) is 3 steps away.
        """

        hex_grid = HexGrid("ne,ne,ne,sw")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.max_distance, 3)
        hex_grid = HexGrid("ne,ne,sw,sw")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.max_distance, 2)
        hex_grid = HexGrid("ne,ne,s,s")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.max_distance, 2)
        hex_grid = HexGrid("se,sw,se,sw,sw")
        hex_grid.find_the_child()
        self.assertEqual(hex_grid.max_distance, 3)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
