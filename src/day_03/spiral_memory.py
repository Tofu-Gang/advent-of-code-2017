__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


################################################################################

class SpiralMemory:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    ROW = "ROW"
    COLUMN = "COLUMN"
    EXPAND = "EXPAND"
    SPIRAL_NEXT = "SPIRAL_NEXT"
    EMPTY_SQUARE = 0
    SPIRAL_ORIGIN = 1

################################################################################

    def __init__(self):
        """
        Create a new memory grid with just the initial square.
        """

        # position of the square at the current end of the spiral
        self._current_row = 0
        self._current_column = 0
        # square 1 position
        self._origin_row = 0
        self._origin_column = 0
        # number of squares forming the spiral
        self._square_counter = self.SPIRAL_ORIGIN
        # direction that was used for movement in the grid to create the last
        # square
        self._direction = self.DOWN
        # the memory grid
        self._memory = [[self._square_counter]]

        # for each direction:
        # -ROW and COLUMN: how should the current position change to move in
        #  the specified direction
        # -EXPAND: expand the grid in the specified direction and add a new
        #  row or column of empty values
        # -SPIRAL_NEXT: what is the next direction from the specified one to
        #  move in a spiral pattern
        self.DIRECTIONS = {
            self.LEFT: {
                self.ROW: lambda: self._current_row,
                self.COLUMN: lambda: self._current_column - 1,
                self.EXPAND: self._expand_left,
                self.SPIRAL_NEXT: self.DOWN
            },
            self.RIGHT: {
                self.ROW: lambda: self._current_row,
                self.COLUMN: lambda: self._current_column + 1,
                self.EXPAND: self._expand_right,
                self.SPIRAL_NEXT: self.UP
            },
            self.UP: {
                self.ROW: lambda: self._current_row - 1,
                self.COLUMN: lambda: self._current_column,
                self.EXPAND: self._expand_up,
                self.SPIRAL_NEXT: self.LEFT
            },
            self.DOWN: {
                self.ROW: lambda: self._current_row + 1,
                self.COLUMN: lambda: self._current_column,
                self.EXPAND: self._expand_down,
                self.SPIRAL_NEXT: self.RIGHT
            }
        }

################################################################################

    @property
    def data_distance(self) -> int:
        """
        :return: Manhattan distance between the last created square (end of the
        spiral) and the memory origin (beginning of the spiral)
        """

        return (abs(self._current_row - self._origin_row)
                + abs(self._current_column - self._origin_column))

################################################################################

    def create_squares(self, square_count: int) -> None:
        """
        Create squares in a spiral pattern, starting in the origin (square 1).
        Square counter increases with each square created by one. This value is
        stored in each square. Create squares until square counter is equal to
        the input value.

        :param square_count: how many squares should be created; value less than
        one has no effect
        """

        if square_count >= self.SPIRAL_ORIGIN:
            while self._square_counter < square_count:
                self._create_square()

################################################################################

    def reset(self) -> None:
        """
        Wipe the memory and reset everything to initial state.
        """

        self._current_row = 0
        self._current_column = 0
        self._origin_row = 0
        self._origin_column = 0
        self._square_counter = self.SPIRAL_ORIGIN
        self._direction = self.DOWN
        self._memory = [[self._square_counter]]

################################################################################

    def _create_square(self) -> None:
        """
        Figure out the direction in which to move in the grid to follow a spiral
        pattern. Expand the grid if needed. Create a new square.
        """

        # what should be the next direction to continue in the spiral pattern
        next_direction = self.DIRECTIONS[self._direction][self.SPIRAL_NEXT]

        if self._needs_expansion(next_direction):
            # grid end reached; change direction and expand the grid so the
            # spiral can continue
            self._direction = next_direction
            self.DIRECTIONS[self._direction][self.EXPAND]()
        else:
            if self._is_next_cell_empty(next_direction):
                # next grid cell (following the spiral pattern) is free to
                # create a new square; change direction
                self._direction = next_direction
            elif self._needs_expansion(self._direction):
                # next grid cell (following the spiral pattern) is already
                # allocated; keep the previous direction
                # grid end reached; expand it so the spiral can continue
                self.DIRECTIONS[self._direction][self.EXPAND]()

        # move to the next cell in the grid
        self._current_row = self.DIRECTIONS[self._direction][self.ROW]()
        self._current_column = self.DIRECTIONS[self._direction][self.COLUMN]()
        # create a new square here
        self._square_counter += 1
        self._memory[self._current_row][self._current_column] = self._square_counter

################################################################################

    def _needs_expansion(self, direction: str) -> bool:
        """
        :param direction: what direction from the current position is tested
        :return: True if movement in the specified direction is not possible due
        to grid edge; False otherwise
        """

        next_row = self.DIRECTIONS[direction][self.ROW]()
        next_column = self.DIRECTIONS[direction][self.COLUMN]()
        return (next_row < 0 or next_row >= len(self._memory)
                or next_column < 0 or next_column >= len(self._memory[0]))

################################################################################

    def _is_next_cell_empty(self, direction: str) -> bool:
        """
        :param direction: what direction from the current position is tested
        :return: True if the cell in the specified direction is free to create
        a new square, False otherwise
        """

        next_row = self.DIRECTIONS[direction][self.ROW]()
        next_column = self.DIRECTIONS[direction][self.COLUMN]()
        return self._memory[next_row][next_column] == self.EMPTY_SQUARE

################################################################################

    def _expand_left(self) -> None:
        """
        Add a new column to the left side of the grid. Adjust current square and
        spiral origin column number.
        """

        [row.insert(0, self.EMPTY_SQUARE) for row in self._memory]
        self._current_column += 1
        self._origin_column += 1

################################################################################

    def _expand_right(self) -> None:
        """
        Add a new column to the right side of the grid.
        """

        [row.append(self.EMPTY_SQUARE) for row in self._memory]

################################################################################

    def _expand_up(self) -> None:
        """
        Add a new row to the top of the grid. Adjust current square and spiral
        origin row number.
        """

        self._memory.insert(0, [self.EMPTY_SQUARE] * len(self._memory[0]))
        self._current_row += 1
        self._origin_row += 1

################################################################################

    def _expand_down(self) -> None:
        """
        Add a new row to the bottom of the grid.
        """

        self._memory.append([self.EMPTY_SQUARE] * len(self._memory[0]))

################################################################################

    def print_memory(self) -> None:
        """

        """
        print("##############################################")
        print("origin:", self._origin_row, self._origin_column)
        for row in self._memory:
            print(row)
        print("##############################################")

################################################################################
