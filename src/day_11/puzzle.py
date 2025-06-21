__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a 
program comes up to you, clearly in distress. "It's my child process," she says, 
"he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.
"""

from src.day_11.hex_grid import HexGrid
from src.utils.utils import print_puzzle_solution


################################################################################

INPUT_FILE_PATH = "src/day_11/input.txt"

################################################################################

def puzzle_01() -> None:
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

    You have the path the child process took. Starting where he started, you
    need to determine the fewest number of steps required to reach him. (A
    "step" means to move from the hex you are in to any adjacent hex.)

    For example:
    -ne,ne,ne is 3 steps away.
    -ne,ne,sw,sw is 0 steps away (back where you started).
    -ne,ne,s,s is 2 steps away (se,se).
    -se,sw,se,sw,sw is 3 steps away (s,s,sw).

    :return: None; Answer should be 670.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        hex_grid = HexGrid(f.read().strip())
        hex_grid.find_the_child()
        print_puzzle_solution(hex_grid.distance)

################################################################################

def puzzle_02() -> None:
    """
    How many steps away is the furthest he ever got from his starting position?

    :return: None; Answer should be 1426.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        hex_grid = HexGrid(f.read().strip())
        hex_grid.find_the_child()
        print_puzzle_solution(hex_grid.max_distance)

################################################################################
