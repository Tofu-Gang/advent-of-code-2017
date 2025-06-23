__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""

"""

from src.day_13.firewall import Firewall
from src.utils.utils import print_puzzle_solution


################################################################################

INPUT_FILE_PATH = "src/day_13/input.txt"

################################################################################

def puzzle_01() -> None:
    """
    :return: None; Answer should be 788.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        # lines = "0: 3\n1: 2\n4: 4\n6: 4".split("\n")
        firewall = Firewall(lines)
        firewall.move_packet()
        print_puzzle_solution(firewall.severity)

################################################################################

def puzzle_02() -> None:
    """
    :return: None; Answer should be .

    1000 too low
    """

    with open(INPUT_FILE_PATH, "r") as f:
        # lines = f.readlines()
        lines = "0: 3\n1: 2\n4: 4\n6: 4".split("\n")
        firewall = Firewall(lines)
        delay = 1
        while True:
            # print("----------------------------------------")
            # print(delay)
            # firewall.print()
            # print("----------------------------------------")
            firewall.delay_packet(delay)
            firewall.move_packet()
            if firewall.caught:
                firewall.reset()
                delay += 1
            else:
                break
        print_puzzle_solution(delay)

################################################################################
