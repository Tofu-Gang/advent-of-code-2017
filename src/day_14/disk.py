__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List, Tuple

from src.day_10.knot_hash import KnotHash


################################################################################

class Disk:
    USED_BIN = "1"
    USED = "#"
    FREE_BIN = "0"
    FREE = "."
    HASH_INPUT_LENGTH = 256
    BIN_PREFIX_LENGTH = 2
    BITS_COUNT = 4
    GRID_HEIGHT = 128
    GRID_WIDTH = 128

################################################################################

    def __init__(self, hash_input: str):
        """

        """

        self._hash_input = hash_input
        self._grid = list(
            list(self._knot_hash_bin(self._knot_hash(row))
                 .replace(self.FREE_BIN, self.FREE)
                 .replace(self.USED_BIN, self.USED))
            for row in range(self.GRID_HEIGHT))
        self._groups = self._get_groups()

################################################################################

    @property
    def used_count(self) -> int:
        """
        :return:
        """

        return sum(row.count(self.USED) for row in self._grid)

################################################################################

    @property
    def groups_count(self) -> int:
        """
        :return:
        """

        return len(self._groups)

################################################################################

    def _knot_hash(self, row: int) -> str:
        """
        :param row:
        :return:
        """

        lengths = f"{self._hash_input}-{row}"
        hash_input = tuple(i for i in range(self.HASH_INPUT_LENGTH))
        return KnotHash(lengths, hash_input).knot_hash

################################################################################

    def _knot_hash_bin(self, knot_hash_hex: str) -> str:
        """
        :param knot_hash_hex:
        :return:
        """

        return "".join(
            bin(int(value, 16))[self.BIN_PREFIX_LENGTH:].zfill(self.BITS_COUNT)
            for value in knot_hash_hex)

################################################################################

    def _get_group(self, row: int, column: int, group: List[Tuple[int, int]]) \
            -> Tuple[Tuple[int, int], ...]:
        """

        :param row:
        :param column:
        :param group:
        :return:
        """

        if self._grid[row][column] == self.USED:
            group.append((row, column))
        if row > 0 and self._grid[row - 1][column] == self.USED and (row - 1, column) not in group:
            group += self._get_group(row - 1, column, group)
        if row < self.GRID_HEIGHT - 1 and self._grid[row + 1][column] == self.USED and (row + 1, column) not in group:
            group += self._get_group(row + 1, column, group)
        if column > 0 and self._grid[row][column - 1] == self.USED and (row, column - 1) not in group:
            group += self._get_group(row, column - 1, group)
        if column < self.GRID_WIDTH - 1 and self._grid[row][column + 1] == self.USED and (row, column + 1) not in group:
            group += self._get_group(row, column + 1, group)
        return tuple(set(group))

################################################################################

    def _get_groups(self) -> List[List[int]]:
        """

        :return:
        """

        groups = []

        for row in range(self.GRID_HEIGHT):
            for column in range(self.GRID_WIDTH):
                if self._grid[row][column] == self.USED:
                    group = self._get_group(row, column, [])
                    for coords in group:
                        self._grid[coords[0]][coords[1]] = self.FREE
                    groups.append(group)

        for group in groups:
            for coords in group:
                self._grid[coords[0]][coords[1]] = self.USED

        return groups

################################################################################
