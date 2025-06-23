__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List
from src.day_13.layer import Layer


################################################################################

class Firewall:
    DENOMINATOR = ":"

################################################################################

    def __init__(self, layer_records: List[str]):
        """

        """

        self._layers = dict()
        self._parse_layers(layer_records)
        self._packet_position = -1
        self._delay = 0
        self._severity = 0
        self._caught = False

################################################################################

    @property
    def delay(self) -> int:
        """
        :return:
        """

        return self._delay

################################################################################

    @property
    def severity(self) -> int:
        """
        :return:
        """

        return self._severity

################################################################################

    def move_packet(self, hard_break: bool) -> None:
        """

        :param hard_break:
        """

        for depth in range(max(self._layers.keys()) + 1):
            self._packet_position += 1
            try:
                layer = self._layers[self._packet_position]

                if layer.security_scanner_pos == 0:
                    self._severity += self._packet_position * layer.range
                    self._caught = True

                    if hard_break:
                        return
            except KeyError:
                pass
            [self._layers[layer].step(1)
             for layer in self._layers
             if layer >= self._packet_position]

################################################################################

    def move_packet_safely(self) -> None:
        """

        """

        while True:
            [layer.step(self._delay) for layer in self._layers.values()]
            self.move_packet(True)
            if self._caught:
                self._reset()
                self._delay += 1
            else:
                break

################################################################################

    def _reset(self) -> None:
        """

        """

        [layer.reset() for layer in self._layers.values()]
        self._packet_position = -1
        self._severity = 0
        self._caught = False

################################################################################

    def _parse_layers(self, layer_records: List[str]) -> None:
        """

        :param layer_records:
        """

        for layer_record in layer_records:
            depth, layer_range = map(int, layer_record.split(self.DENOMINATOR))
            self._layers[depth] = Layer(layer_range)

################################################################################
