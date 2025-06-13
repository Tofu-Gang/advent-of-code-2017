__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List
from re import compile
from src.day_07.program import Program


################################################################################

class Tower:
    DIVIDER = "->"

################################################################################

    def __init__(self, lines: List[str]):
        """
        Create a tower of programs from the input data.

        :param lines: programs information
        """

        self._programs = dict()
        self._load_programs(lines)

################################################################################

    def get_bottom_program(self) -> Program:
        """
        :return: a program that is at the bottom of the tower
        """

        program = tuple(self._programs.values())[0]
        while program.supporter is not None:
            program = program.supporter
        return program

################################################################################

    def get_balanced_weight(self) -> int | None:
        """
        :return: one program in the tower is unbalanced; find it and get the
        weight it should have to make this tower balanced
        """

        for program in self._programs.values():
            if not program.is_balanced:
                return program.balanced_weight
        return None

################################################################################

    def _load_programs(self, lines: List[str]) -> None:
        """
        Create programs from the input data and link them together.

        :param lines: programs input data
        """

        # for each input line, create a program and store it in a dictionary
        # under its name
        for line in lines:
            name = line.split()[0]
            weight = int(compile(r"\d+").search(line.strip()).group(0))
            program = Program(name, weight)
            self._programs[name] = program

        # now that all programs are created, for each program, add links to
        # programs that are held on its disc (a sub-tower)
        for line in tuple(filter(lambda line: self.DIVIDER in line, lines)):
            name = line.split()[0]
            program = self._programs[name]
            holding_list = tuple(
                map(str.strip, line.split(self.DIVIDER)[1].split(",")))
            [program.add_program(self._programs[name]) for name in holding_list]

        # finally, for each program, add a link to the program that holds it on
        # its disc
        for program in self._programs.values():
            for supported in program.holding:
                supported.set_supporter(program)

################################################################################
