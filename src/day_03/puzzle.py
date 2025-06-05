__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite 
two-dimensional grid.
"""

from src.utils.utils import print_puzzle_solution


################################################################################

PUZZLE_INPUT = "312051"

################################################################################

class SpiralMemory:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    ROW = "ROW"
    COLUMN = "COLUMN"
    EXPAND = "EXPAND"

    PRIORITY = {
        DOWN: RIGHT,
        RIGHT: UP,
        UP: LEFT,
        LEFT: DOWN
    }

    EMPTY = 0

    def __init__(self):
        """

        """

        self._counter = 1
        self._row = 0
        self._column = 0
        self._direction = self.DOWN
        self._memory = [[self._counter]]

        self.DIRECTIONS = {
            self.LEFT: {
                self.ROW: lambda row: row,
                self.COLUMN: lambda column: column - 1,
                self.EXPAND: self._expand_left
            },
            self.RIGHT: {
                self.ROW: lambda row: row,
                self.COLUMN: lambda column: column + 1,
                self.EXPAND: self._expand_right
            },
            self.UP: {
                self.ROW: lambda row: row - 1,
                self.COLUMN: lambda column: column,
                self.EXPAND: self._expand_up
            },
            self.DOWN: {
                self.ROW: lambda row: row + 1,
                self.COLUMN: lambda column: column,
                self.EXPAND: self._expand_down
            }
        }

################################################################################

    def make_step(self) -> None:
        """

        """

        priority = self.PRIORITY[self._direction]

        if not self._needs_expansion(priority):
            if self._memory[next_row][next_column] == self.EMPTY:
                self._counter += 1
                self._row = next_row
                self._column = next_column
                self._memory[self._row][self._column] = self._counter
            else:
                next_row = self.DIRECTIONS[self._direction][self.ROW]
                next_column = self.DIRECTIONS[self._direction][self.COLUMN]

                if next_row < len(self._memory) and next_column < len(self._memory[0]):
                    pass
                else:
                    pass
        else:
            pass


################################################################################

    def print_memory(self) -> None:
        """

        """

        for row in self._memory:
            print(row)

################################################################################

    def _needs_expansion(self, direction: str) -> bool:
        """
        :return:
        """

        next_row = self.DIRECTIONS[direction][self.ROW]
        next_column = self.DIRECTIONS[direction][self.COLUMN]
        return (0 <= next_row < len(self._memory)
                and 0 <= next_column < len(self._memory[0]))

################################################################################

    def _move(self) -> None:
        """

        """

        self._row = self.DIRECTIONS[self._direction][self.ROW]
        self._column = self.DIRECTIONS[self._direction][self.COLUMN]
        self._counter += 1
        self._memory[self._row][self._column] = self._counter

################################################################################

    def _is_next_cell_empty(self, direction: str) -> bool:
        """

        :param direction:
        :return:
        """

        next_row = self.DIRECTIONS[direction][self.ROW]
        next_column = self.DIRECTIONS[direction][self.COLUMN]
        return self._memory[next_row][next_column] == self.EMPTY

################################################################################

    def _expand_left(self) -> None:
        """

        """

        [row.insert(0, self.EMPTY) for row in self._memory]
        self._column += 1

################################################################################

    def _expand_right(self) -> None:
        """

        """

        [row.append(self.EMPTY) for row in self._memory]

################################################################################

    def _expand_up(self) -> None:
        """

        """

        self._memory.insert(0, [self.EMPTY] * len(self._memory[0]))
        self._row += 1

################################################################################

    def _expand_down(self) -> None:
        """

        """

        self._memory.append([self.EMPTY] * len(self._memory[0]))

################################################################################

def puzzle_01() -> None:
    """
    Each square on the grid is allocated in a spiral pattern starting at a
    location marked 1 and then counting up while spiraling outward. For example,
    the first few squares are allocated like this:
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    While this is very space-efficient (no squares are skipped), requested data
    must be carried back to square 1 (the location of the only access port for
    this memory system) by programs that can only move up, down, left, or right.
    They always take the shortest path: the Manhattan Distance between the
    location of the data and square 1.

    For example:
    -Data from square 1 is carried 0 steps, since it's at the access port.
    -Data from square 12 is carried 3 steps, such as: down, left, left.
    -Data from square 23 is carried only 2 steps: up twice.
    -Data from square 1024 must be carried 31 steps.

    How many steps are required to carry the data from the square identified in
    your puzzle input all the way to the access port?

    :return: None; Answer should be .
    """

    memory = SpiralMemory()
    memory.print_memory()
    memory._expand_right()
    memory.print_memory()
    # with open(INPUT_FILE_PATH, "r") as f:
    #     spreadsheet = f.read()
    #     checksum = get_checksum(spreadsheet)
    #     print_puzzle_solution(checksum)

################################################################################

def puzzle_02() -> None:
    """
    :return: None; Answer should be 263.
    """

    pass
    # with open(INPUT_FILE_PATH, "r") as f:
    #     spreadsheet = f.read()
    #     checksum = get_evenly_divisible_checksum(spreadsheet)
    #     print_puzzle_solution(checksum)

################################################################################
