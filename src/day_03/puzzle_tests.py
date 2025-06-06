__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from spiral_memory import SpiralMemory


class TestDay01(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        -Data from square 1 is carried 0 steps, since it's at the access port.
        -Data from square 12 is carried 3 steps, such as: down, left, left.
        -Data from square 23 is carried only 2 steps: up twice.
        -Data from square 1024 must be carried 31 steps.
        """

        memory = SpiralMemory()
        memory.create_squares(1)
        self.assertEqual(memory.data_distance, 0)
        memory.reset()
        memory.create_squares(12)
        self.assertEqual(memory.data_distance, 3)
        memory.reset()
        memory.create_squares(23)
        self.assertEqual(memory.data_distance, 2)
        memory.reset()
        memory.create_squares(1024)
        self.assertEqual(memory.data_distance, 31)

################################################################################

    def test_puzzle_2(self) -> None:
        """

        """

        pass

################################################################################

if __name__ == '__main__':
    main()

################################################################################
