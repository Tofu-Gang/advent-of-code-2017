__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_10.knot_hash import KnotHash


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        Here's an example using a smaller list:

        Suppose we instead only had a circular list containing five elements, 0,
        1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.
        -The list begins as [0] 1 2 3 4 (where square brackets indicate the
         current position).
        -The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate
         the sublist to be reversed).
        -After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
        -Then, the current position moves forward by the length, 3, plus the
         skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.
        -The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
        -The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
        -The current position moves forward by the length plus the skip size, a
         total of 5, causing it not to move because it wraps around:
         4 3 0 [1] 2. The skip size increases to 2.
        -The third length, 1, selects a sublist of a single element, and so
         reversing it has no effect.
        -The current position moves forward by the length (1) plus the skip size
         (2): 4 [3] 0 1 2. The skip size increases to 3.
        -The fourth length, 5, selects every element starting with the second:
         4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3)
         produces: 3) ([4] 2 1 0.
        -Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip
         size increases to 4.

        In this example, the first two numbers in the list end up being 3 and 4;
        to  check the process, you can multiply them together to produce 12.
        """

        lengths = "3,4,1,5"
        marks = tuple(i for i in range(5))
        knot_hash = KnotHash(lengths, marks)
        self.assertEqual(knot_hash.multiplication, 12)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        Here are some example hashes:
        -The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
        -AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
        -1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
        -1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
        """

        knot_hash = KnotHash("", tuple(i for i in range(256)))
        self.assertEqual(
            knot_hash.knot_hash, "a2582a3a0e66e6e86e3812dcb672a272")
        knot_hash = KnotHash("AoC 2017", tuple(i for i in range(256)))
        self.assertEqual(
            knot_hash.knot_hash, "33efeb34ea91902bb2f59c9920caa6cd")
        knot_hash = KnotHash("1,2,3", tuple(i for i in range(256)))
        self.assertEqual(
            knot_hash.knot_hash, "3efbe78a8d82f29979031a4aa0b16a9d")
        knot_hash = KnotHash("1,2,4", tuple(i for i in range(256)))
        self.assertEqual(
            knot_hash.knot_hash, "63960835bcdc130f0b66d7ff4f6a5a8e")

################################################################################

if __name__ == '__main__':
    main()

################################################################################
