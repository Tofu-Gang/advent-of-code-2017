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
        self._picosecond = 0
        self._severity = 0
        self._caught = False

################################################################################

    def reset(self) -> None:
        """

        """

        [layer.reset() for layer in self._layers.values()]
        self._packet_position = -1
        self._picosecond = 0
        self._severity = 0
        self._caught = False

################################################################################

    @property
    def caught(self) -> bool:
        """
        :return:
        """

        return self._caught

################################################################################

    @property
    def severity(self) -> int:
        """
        :return:
        """

        return self._severity

################################################################################

    def delay_packet(self, picoseconds: int) -> None:
        """

        :param picoseconds:
        """

        self._picosecond = picoseconds

        for _ in range(picoseconds):
            [layer.step() for layer in self._layers.values()]

################################################################################

    def move_packet(self) -> None:
        """

        """

        # print("Initial state:")
        # self.print()

        for depth in range(max(self._layers.keys()) + 1):
            # print("------------------------------------------------------------")
            # print(f"Picosecond: {self._picosecond}, caught: {self._caught}")
            self._packet_position += 1
            # print("packet position:", self._packet_position)
            try:
                layer = self._layers[self._packet_position]
                # print(layer.security_scanner_pos)
                if layer.security_scanner_pos == 0:
                    self._severity += self._packet_position * layer.range
                    self._caught = True
            except KeyError:
                pass
            # self.print()
            [layer.step() for layer in self._layers.values()]
            # self.print()
            self._picosecond += 1

################################################################################

    def print(self) -> None:
        """

        """


        result = " "
        max_depth = max(layer.range for layer in self._layers.values())

        for depth in range(max(self._layers.keys()) + 1):
            result += f"{depth}   "
        result += "\n"
        for layer_range in range(max_depth):
            for depth in range(max(self._layers.keys()) + 1):
                if depth in self._layers and layer_range < self._layers[depth].range:
                    if layer_range == self._layers[depth].security_scanner_pos:
                        if depth == self._packet_position and layer_range == 0:
                            result += "(S) "
                        else:
                            result += "[S] "
                    else:
                        if depth == self._packet_position and layer_range == 0:
                            result += "( ) "
                        else:
                            result += "[ ] "
                else:
                    if depth == self._packet_position and layer_range == 0:
                        result += "( ) "
                    else:
                        result += "    "
            result += "\n"
        print(result)

################################################################################

    def _parse_layers(self, layer_records: List[str]) -> None:
        """

        :param layer_records:
        """

        for layer_record in layer_records:
            depth, layer_range = map(int, layer_record.split(self.DENOMINATOR))
            self._layers[depth] = Layer(layer_range)

################################################################################
