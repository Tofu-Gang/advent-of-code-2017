__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


################################################################################

class Layer:
    UP = "UP"
    DOWN = "DOWN"

################################################################################

    def __init__(self, layer_range: int):
        """

        """

        self._range = layer_range
        self._direction = self.DOWN
        self._security_scanner_pos = 0

################################################################################

    def reset(self) -> None:
        """

        """

        self._direction = self.DOWN
        self._security_scanner_pos = 0

################################################################################

    @property
    def security_scanner_pos(self) -> int:
        """
        :return:
        """

        return self._security_scanner_pos

################################################################################

    @property
    def range(self) -> int:
        """
        :return:
        """

        return self._range

################################################################################

    def step(self, count: int) -> None:
        """

        :param count:
        """

        count %= (self._range + (self._range - 2))

        for _ in range(count):
            if self._direction == self.DOWN:
                if self._security_scanner_pos < self._range - 1:
                    self._security_scanner_pos += 1
                else:
                    self._direction = self.UP
                    self._security_scanner_pos -= 1
            elif self._direction == self.UP:
                if self._security_scanner_pos > 0:
                    self._security_scanner_pos -= 1
                else:
                    self._direction = self.DOWN
                    self._security_scanner_pos += 1

################################################################################
