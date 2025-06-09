__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from maze import Maze


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        For example, consider the following list of jump offsets:
        0
        3
        0
        1
        -3

        Positive jumps ("forward") move downward; negative jumps move upward.
        For legibility in this example, these offset values will be written all
        on one line, with the current instruction marked in parentheses. The
        following steps would be taken before an exit is found:
        (0) 3  0  1  -3  - before we have taken any steps.
        (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
         Fortunately, the instruction is then incremented to 1.
         2 (3) 0  1  -3  - step forward because of the instruction we just
         modified. The first instruction is incremented again, now to 2.
         2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
         2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
         2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

        In this example, the exit is reached in 5 steps.
        """

        instructions = list(map(int, "0\n3\n0\n1\n-3".strip().split("\n")))
        maze = Maze(instructions, False)
        maze.process_instructions()
        self.assertEqual(maze.steps, 5)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, consider the following list of jump offsets:
        0
        3
        0
        1
        -3

        Positive jumps ("forward") move downward; negative jumps move upward.
        For legibility in this example, these offset values will be written all
        on one line, with the current instruction marked in parentheses. The
        following steps would be taken before an exit is found:
        (0) 3  0  1  -3
        (1) 3  0  1  -3
         2 (3) 0  1  -3
         2  2  0  1 (-3)
         2 (2) 0  1  -2
         2  3  0 (1) -2
         2  3  0  2 (-2)
         2  3 (0) 2  -1
         2  3 (1) 2  -1
         2  3  2 (2) -1
         2  3  2  3  -1  x

        The process now takes 10 steps.
        """

        instructions = list(map(int, "0\n3\n0\n1\n-3".strip().split("\n")))
        maze = Maze(instructions, True)
        maze.process_instructions()
        self.assertEqual(maze.steps, 10)


################################################################################

if __name__ == '__main__':
    main()

################################################################################
