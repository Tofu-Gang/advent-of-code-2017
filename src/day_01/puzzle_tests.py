__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from puzzle import get_captcha


class TestDay01(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        -1122 produces a sum of 3 (1 + 2) because the first digit (1) matches
         the second digit and the third digit (2) matches the fourth digit.
        -1111 produces 4 because each digit (all 1) matches the next.
        -1234 produces 0 because no digit matches the next.
        -91212129 produces 9 because the only digit that matches the next one is
         the last digit, 9.
        """

        self.assertEqual(get_captcha("1122", 1), 3)
        self.assertEqual(get_captcha("1111", 1), 4)
        self.assertEqual(get_captcha("1234", 1), 0)
        self.assertEqual(get_captcha("91212129", 1), 9)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        -1212 produces 6: the list contains 4 items, and all four digits match
         the digit 2 items ahead.
        -1221 produces 0, because every comparison is between a 1 and a 2.
        -123425 produces 4, because both 2s match each other, but no other digit
         has a match.
        -123123 produces 12.
        -12131415 produces 4.
        """

        self.assertEqual(self._get_new_captcha_wrapper("1212"), 6)
        self.assertEqual(self._get_new_captcha_wrapper("1221"), 0)
        self.assertEqual(self._get_new_captcha_wrapper("123425"), 4)
        self.assertEqual(self._get_new_captcha_wrapper("123123"), 12)
        self.assertEqual(self._get_new_captcha_wrapper("12131415"), 4)

################################################################################

    def _get_new_captcha_wrapper(self, sequence: str) -> int:
        """
        Wrapper function to keep the code dry.

        :param sequence: input sequence
        :return: new captcha for puzzle 2
        """

        step = int(len(sequence) / 2)
        return get_captcha(sequence, step)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
