__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List
from sys import maxsize


################################################################################

class Registers:
    REGISTERS_VAR_NAME = "self._registers"
    CONDITION_DELIMITER = "if"
    INCREASE_ORIGINAL = "inc"
    DECREASE_ORIGINAL = "dec"
    INCREASE_PYTHON = "+="
    DECREASE_PYTHON = "-="

################################################################################

    def __init__(self, instructions: List[str]):
        """
        Create a dictionary where keys are name of registers and values are
        values stored in those registers. Load instructions that change register
        values. Each instruction contains a condition and executes only when
        this condition is true.

        :param instructions: instructions that change register values
        """

        self._registers = dict()
        self._instructions = instructions
        self._max_continuous_value = -maxsize - 1

################################################################################

    @property
    def max_continuous_register_value(self) -> int:
        """
        :return: the highest value ever held in any register during instructions
        evaluation
        """

        return self._max_continuous_value

################################################################################

    @property
    def max_register_value(self) -> int:
        """
        :return: the highest value held in any register after instructions
        evaluation
        """

        return max(self._registers.values())

################################################################################

    def run_instructions(self) -> None:
        """
        Go through all instructions and for each one:
        -make sure all referenced registers exist
        -evaluate its condition
        -if the condition is true, modify a registry value
        -check if any register value reached a new maximum; if so, mark it
        """

        for instruction in self._instructions:
            self._prevent_null_pointer(instruction)

            if self._is_condition_true(instruction):
                exec(self._convert_to_python(instruction))

            current_max_value = max(self._registers.values())

            if self._max_continuous_value < current_max_value:
                self._max_continuous_value = current_max_value

################################################################################

    def _convert_to_python(self, instruction: str) -> str:
        """
        :param instruction: original instruction from the input
        :return: part of the instruction that modifies a registry value
        converted to Python syntax
        """

        modification = instruction.split(self.CONDITION_DELIMITER)[0].strip()
        register_name = modification.split()[0].strip()
        return (modification
                .replace(
            register_name,
            f"{self.REGISTERS_VAR_NAME}['{register_name}']", 1)
                .replace(
            self.INCREASE_ORIGINAL,
            self.INCREASE_PYTHON, 1)
                .replace(
            self.DECREASE_ORIGINAL,
            self.DECREASE_PYTHON, 1))

################################################################################

    def _is_condition_true(self, instruction: str) -> bool:
        """
        :param instruction: original instruction from the input
        :return: condition evaluation result
        """

        condition = instruction.split(self.CONDITION_DELIMITER)[1].strip()
        register_name = condition.split()[0]

        if register_name not in self._registers:
            self._registers[register_name] = 0

        return eval(condition.replace(
            register_name,
            f"{self.REGISTERS_VAR_NAME}['{register_name}']"))

################################################################################

    def _prevent_null_pointer(self, instruction) -> None:
        """
        Get register names from both the modification and condition parts of the
        input instruction. Make sure these registers exist. If needed, create a
        new register and init its value to zero.

        :param instruction: original instruction from the input
        """

        parts = instruction.split(self.CONDITION_DELIMITER)
        modification = parts[0].strip()
        condition = parts[1].strip()
        modification_register_name = modification.split()[0].strip()
        condition_register_name = condition.split()[0].strip()

        if modification_register_name not in self._registers:
            self._registers[modification_register_name] = 0
        if condition_register_name not in self._registers:
            self._registers[condition_register_name] = 0

################################################################################
