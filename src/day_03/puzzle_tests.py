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
        -Square 1 starts with the value 1.
        -Square 2 has only one adjacent filled square (with value 1), so it also
         stores 1.
        -Square 3 has both of the above squares as neighbors and stores the sum
         of their values, 2.
        -Square 4 has all three of the aforementioned squares as neighbors and
         stores the sum of their values, 4.
        -Square 5 only has the first and fourth squares as neighbors, so it gets
         the value 5.
        """

        memory = SpiralMemory()
        memory.stress_test(1)
        self.assertEqual(memory.current_square, 1)
        memory.reset()
        memory.stress_test(2)
        self.assertEqual(memory.current_square, 2)
        memory.reset()
        memory.stress_test(4)
        self.assertEqual(memory.current_square, 4)
        memory.reset()
        memory.stress_test(5)
        self.assertEqual(memory.current_square, 5)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
