__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List, Self


################################################################################

class Program:

    def __init__(self, name: str, weight: int):
        """
        Each program has a name, its weight and a disc which may hold any number
        of other programs. In reverse, each program (except for the bottom one)
        is held on a disc of one other program.

        :param name:
        :param weight:
        """

        self._name = name
        self._weight = weight
        self._holding = []
        self._supporter = None

################################################################################

    @property
    def name(self) -> str:
        """
        :return: program name
        """

        return self._name

################################################################################

    @property
    def weight(self) -> int:
        """
        :return: program weight
        """

        return self._weight

################################################################################

    @property
    def sub_tower_weight(self) -> int:
        """
        :return: weight of all programs this one is holding on its disc
        including its own weight
        """

        return (sum(program.sub_tower_weight for program in self._holding)
                + self._weight)

################################################################################

    @property
    def holding(self) -> List[Self]:
        """
        :return: list of programs this one is holding on its disc
        """

        return self._holding

################################################################################

    @property
    def supporter(self) -> Self | None:
        """
        :return: the program that holds this one on its disc or None if this is
        the bottom program
        """

        return self._supporter

################################################################################

    @property
    def is_balanced(self) -> bool:
        """
        :return: True if all sub-towers this program is holding on its disc have
        the same weight, False otherwise; program that hold zero programs on its
        disc are considered balanced
        """

        try:
            sub_tower_weights = tuple(
                program.sub_tower_weight for program in self._holding)
            return min(sub_tower_weights) == max(sub_tower_weights)
        except ValueError:
            return True

################################################################################

    @property
    def balanced_weight(self) -> int:
        """
        Find the program that makes this one unbalanced. Count the correct
        weight the program should have to make this one balanced.

        :return: correct weight of a program that makes this one unbalanced;
        weight of any program on this program's disc if this program is
        balanced; zero for a program with no programs on its disc
        """

        try:
            # get minimum and maximum sub-tower weights
            sub_tower_weights = tuple(
                program.sub_tower_weight for program in self._holding)
            min_weight = min(sub_tower_weights)
            max_weight = max(sub_tower_weights)

            if list(sub_tower_weights).count(min_weight) == 1:
                # the sub-tower with maximum weight makes the program unbalanced
                unbalanced = next(filter(
                    lambda program: program.sub_tower_weight == min_weight,
                    self._holding))
                return unbalanced.weight + (max_weight - min_weight)
            elif list(sub_tower_weights).count(max_weight) == 1:
                # the sub-tower with minimum weight makes the program unbalanced
                unbalanced = next(filter(
                    lambda program: program.sub_tower_weight == max_weight,
                    self._holding))
                return unbalanced.weight - (max_weight - min_weight)
            else:
                # this program is balanced
                return self._holding[0].weight
        except ValueError:
            # no sub-towers on this program's disc
            return 0

################################################################################

    def add_program(self, program: Self) -> None:
        """
        :param program: add a program to the sub-tower this program holds on its
        disc
        """

        self._holding.append(program)

################################################################################

    def set_supporter(self, supporter: Self) -> None:
        """
        Add a link to the program that holds this program on its disc.

        :param supporter: the program that holds this program on its disc
        """

        self._supporter = supporter

################################################################################
