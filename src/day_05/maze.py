__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List


################################################################################

class Maze:

    def __init__(self, instructions: List[int], stranger: bool):
        """
        Create a maze from a list of instructions. Each instruction is the
        offset for each jump. Jumps are relative: -1 moves to the previous
        instruction, 2 skips the next one and so on. Start at the first
        instruction in the list. The goal is to follow the jumps until one leads
        outside the list.

        After each jump, the offset of that instruction changes.

        For puzzle 1, it always increases by 1. So, if you come across an offset
        of 3, you would move three instructions forward, but change it to a 4
        for the next time it is encountered.

        For puzzle 2, after each jump, if the offset was three or more, decrease
        it by 1. Otherwise, increase it by 1 as for puzzle 1.

        :param instructions: list of instructions
        :param stranger: True for puzzle 2, False for puzzle 1
        """

        self._maze = instructions
        # start at the first instruction in the list
        self._counter = 0
        # count how many steps it takes to jump out of the maze
        self._steps = 0
        # True for puzzle 2, False for puzzle 1
        self._stranger = stranger

################################################################################

    def process_instructions(self) -> None:
        """
        Perform jumps according to each instruction until the counter jumps
        outside the maze.
        """

        while not self._is_outside():
            self._jump()

################################################################################

    @property
    def steps(self) -> int:
        """
        :return: number of steps needed to jump outside the maze
        """

        return self._steps

################################################################################

    def _jump(self) -> None:
        """
        Get the offset of the current instruction. Then the instruction changes.

        For puzzle 1, it always increases by 1. So, if you come across an offset
        of 3, you would move three instructions forward, but change it to a 4
        for the next time it is encountered.

        For puzzle 2, if the offset was three or more, decrease it by 1.
        Otherwise, increase it by 1 as for puzzle 1.

        Then jump to the next instruction by the original offset.
        """

        offset = self._maze[self._counter]
        if self._stranger and offset >= 3:
            # puzzle 2
            self._maze[self._counter] -= 1
        else:
            # puzzle 1
            self._maze[self._counter] += 1
        self._counter += offset
        self._steps += 1

################################################################################

    def _is_outside(self) -> bool:
        """
        :return: True if the counter is outside the maze, False otherwise
        """

        return self._counter < 0 or self._counter >= len(self._maze)

################################################################################
