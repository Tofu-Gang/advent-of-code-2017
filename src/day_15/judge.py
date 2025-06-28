__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


from src.day_15.dueling_generator import DuelingGenerator

################################################################################

class Judge:
    BITS_TO_COMPARE = 16

################################################################################

    def __init__(self, gen_a: DuelingGenerator, gen_b: DuelingGenerator, pairs_count: int):
        """

        """

        self._generator_a = gen_a
        self._generator_b = gen_b
        self._pairs_count = pairs_count
        self._matches = 0

################################################################################

    @property
    def matches(self) -> int:
        """
        :return:
        """

        return self._matches

################################################################################

    def generate_pairs(self) -> None:
        """

        """

        for _ in range(self._pairs_count):
            self._generate_pair()

################################################################################

    def _generate_pair(self) -> None:
        """

        """

        value_a = next(self._generator_a)
        value_b = next(self._generator_b)
        to_compare_a = bin(value_a)[2:].zfill(32)[-self.BITS_TO_COMPARE:]
        to_compare_b = bin(value_b)[2:].zfill(32)[-self.BITS_TO_COMPARE:]
        self._matches += 1 if to_compare_a == to_compare_b else 0

################################################################################
