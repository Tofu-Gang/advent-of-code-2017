__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from sys import maxsize


################################################################################

class HexGrid:
    """
    The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
    be found to the north, northeast, southeast, south, southwest, and
    northwest:
     \\ n  /
    nw +--+ ne
      /   \\
    -+      +-
     \\    /
    sw +--+ se
      / s \\
    """

    N = "n"
    NE = "ne"
    SE = "se"
    S = "s"
    SW = "sw"
    NW = "nw"
    DIRECTIONS = (N, NE, SE, S, SW, NW)
    SEPARATOR = ","

################################################################################

    def __init__(self, directions: str):
        """
        Having the path the child process took, we need to determine:
        -the fewest number of steps in the hex grid required to reach him
        -how many steps away is the furthest he ever got from his starting
         position

        :param directions: the path the child process took
        """

        self._directions = directions.split(self.SEPARATOR)
        self._max_distance = -maxsize - 1
        self._distance = -maxsize - 1

################################################################################

    def find_the_child(self) -> None:
        """
        Tracking the path the child process took step by step, we create and
        constantly modify the shortest path that gets us to his current
        position. We also track the furthest he ever got from the starting
        position.

        Some pairs of directions cancel each other out completely, sometimes the
        pair can be replaced with just one step in one direction. For example
        for the NORTH direction:
        -cancels out with SOUTH completely
        -a combination with SOUTH WEST can be replaced with just one step in
         NORTH WEST direction
        -a combination with SOUTH EAST can be replaced with just one step in
         NORTH EAST direction

        Having arranged the directions in a (circular) list, the complements and
        replacements for each direction can be found on the same relative
        position in the list.
        """

        shortest_path = []

        for direction in self._directions:
            shortest_path.append(direction)
            index = self.DIRECTIONS.index(direction)
            # get complements and replacements for the current direction
            opposite = self.DIRECTIONS[(index + 3) % len(self.DIRECTIONS)]
            left_cancels = self.DIRECTIONS[(index + 4) % len(self.DIRECTIONS)]
            left_makes = self.DIRECTIONS[(index + 5) % len(self.DIRECTIONS)]
            right_cancels = self.DIRECTIONS[(index + 2) % len(self.DIRECTIONS)]
            right_makes = self.DIRECTIONS[(index + 1) % len(self.DIRECTIONS)]

            if opposite in shortest_path:
                # these two steps cancel each other out completely, remove them
                shortest_path.remove(direction)
                shortest_path.remove(opposite)
            elif left_cancels in shortest_path:
                # these two steps can be replaced with just one step
                shortest_path.remove(direction)
                shortest_path.remove(left_cancels)
                shortest_path.append(left_makes)
            elif right_cancels in shortest_path:
                # these two steps can be replaced with just one step
                shortest_path.remove(direction)
                shortest_path.remove(right_cancels)
                shortest_path.append(right_makes)

            self._max_distance = max(self._max_distance, len(shortest_path))
        self._distance = len(shortest_path)

################################################################################

    @property
    def distance(self) -> int:
        """
        :return: the fewest number of steps required to reach the child process
        """

        return self._distance

################################################################################

    @property
    def max_distance(self) -> int:
        """
        :return: furthest the child process ever got from his starting position
        """

        return self._max_distance

################################################################################
