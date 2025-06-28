__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


################################################################################

class DuelingGenerator:
    DIVISOR = 2147483647

################################################################################

    def __init__(self, initial_value: int, factor: int, multiple: int=1):
        """

        :param initial_value:
        :param factor:
        :param multiple:
        """

        self._current_value = initial_value
        self._factor = factor
        self._multiple = multiple

################################################################################

    def __next__(self):
        """

        :return:
        """

        while True:
            self._current_value = (self._current_value * self._factor) % self.DIVISOR

            if self._current_value % self._multiple == 0:
                break
        return self._current_value

################################################################################
