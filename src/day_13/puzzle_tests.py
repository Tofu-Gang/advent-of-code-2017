__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_13.firewall import Firewall


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """

        """

        lines = "0: 3\n1: 2\n4: 4\n6: 4".split("\n")
        firewall = Firewall(lines)
        firewall.move_packet(False)
        self.assertEqual(firewall.severity, 24)

################################################################################

    def test_puzzle_2(self) -> None:
        """

        """

        lines = "0: 3\n1: 2\n4: 4\n6: 4".split("\n")
        firewall = Firewall(lines)
        firewall.move_packet_safely()
        self.assertEqual(firewall.delay, 10)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
