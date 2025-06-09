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

    @property
    def current_square(self) -> int:
        """
        :return: current square value
        """

        return self._memory[self._current_row][self._current_column]

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
                self._create_square(False)

################################################################################

    def stress_test(self, threshold: int) -> None:
        """
        Create squares in a spiral pattern, starting in the origin (square 1).
        A sum of all adjacent values (8 directions) is written to each new
        square.

        :param threshold: stress test is stopped first time the value written in
        a new square is larger than this param
        """

        if threshold > self.SPIRAL_ORIGIN:
            while self.current_square < threshold:
                self._create_square(True)

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

    def _create_square(self, stress_test: bool) -> None:
        """
        Figure out the direction in which to move in the grid to follow a spiral
        pattern. Expand the grid if needed. Create a new square.

        :param stress_test: True for puzzle 2, False for puzzle 1
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

        if stress_test:
            # puzzle 2
            self._write(self._get_adjacent_sum())
        else:
            # puzzle 1
            self._write(self._square_counter)

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

    def _get_adjacent_sum(self) -> int:
        """
        :return: sum of all adjacent squares of the current square
        """

        result = 0
        result += self._get_top_left()
        result += self._get_up()
        result += self._get_top_right()
        result += self._get_right()
        result += self._get_bottom_right()
        result += self._get_bottom()
        result += self._get_bottom_left()
        result += self._get_left()
        return result

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

    def _write(self, value: int) -> None:
        """
        Write a value to the current position in the memory.

        :param value: value to be written in the memory
        """

        self._memory[self._current_row][self._current_column] = value

################################################################################

    def _get_top_left(self) -> int:
        """
        :return: data from the square to the left and up from the current one or
        zero if the square does not exist
        """

        if self._current_row > 0 and self._current_column > 0:
            return self._memory[self._current_row - 1][self._current_column - 1]
        else:
            return 0

################################################################################

    def _get_up(self) -> int:
        """
        :return: data from the square up from the current one or zero if the
        square does not exist
        """

        if self._current_row > 0:
            return self._memory[self._current_row - 1][self._current_column]
        else:
            return 0

################################################################################

    def _get_top_right(self) -> int:
        """
        :return: data from the square to the right and up from the current one
        or zero if the square does not exist
        """

        if (self._current_row > 0
                and self._current_column < len(self._memory[0]) - 1):
            return self._memory[self._current_row - 1][self._current_column + 1]
        else:
            return 0

################################################################################

    def _get_right(self) -> int:
        """
        :return: data from the square to the right from the current one or zero
        if the square does not exist
        """

        if self._current_column < len(self._memory[0]) - 1:
            return self._memory[self._current_row][self._current_column + 1]
        else:
            return 0

################################################################################

    def _get_bottom_right(self) -> int:
        """
        :return: data from the square to the right and down from the current one
        or zero if the square does not exist
        """

        if (self._current_row < len(self._memory) - 1
                and self._current_column < len(self._memory[0]) - 1):
            return self._memory[self._current_row + 1][self._current_column + 1]
        else:
            return 0

################################################################################

    def _get_bottom(self) -> int:
        """
        :return: data from the square down from the current one or zero if the
        square does not exist
        """

        if self._current_row < len(self._memory) - 1:
            return self._memory[self._current_row + 1][self._current_column]
        else:
            return 0

################################################################################

    def _get_bottom_left(self) -> int:
        """
        :return: data from the square to the left and down from the current one
        or zero if the square does not exist
        """

        if (self._current_row < len(self._memory) - 1
                and self._current_column > 0):
            return self._memory[self._current_row + 1][self._current_column - 1]
        else:
            return 0

################################################################################

    def _get_left(self) -> int:
        """
        :return: data from the square to the left from the current one or zero
        if the square does not exist
        """

        if self._current_column > 0:
            return self._memory[self._current_row][self._current_column - 1]
        else:
            return 0

################################################################################
