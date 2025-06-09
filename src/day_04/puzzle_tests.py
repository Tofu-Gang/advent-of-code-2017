__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from puzzle import is_passphrase_valid, is_passphrase_valid_anagrams


class TestDay01(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        -aa bb cc dd ee is valid.
        -aa bb cc dd aa is not valid - the word aa appears more than once.
        -aa bb cc dd aaa is valid - aa and aaa count as different words.
        """

        self.assertTrue(is_passphrase_valid("aa bb cc dd ee"))
        self.assertFalse(is_passphrase_valid("aa bb cc dd aa"))
        self.assertTrue(is_passphrase_valid("aa bb cc dd aaa"))

################################################################################

    def test_puzzle_2(self) -> None:
        """
        -abcde fghij is a valid passphrase.
        -abcde xyz ecdab is not valid - the letters from the third word can be
         rearranged to form the first word.
        -a ab abc abd abf abj is a valid passphrase, because all letters need to
         be used when forming another word.
        -iiii oiii ooii oooi oooo is valid.
        -oiii ioii iioi iiio is not valid - any of these words can be rearranged
         to form any other word.
        """

        self.assertTrue(is_passphrase_valid_anagrams("abcde fghij"))
        self.assertFalse(is_passphrase_valid_anagrams("abcde xyz ecdab"))
        self.assertTrue(is_passphrase_valid_anagrams("a ab abc abd abf abj"))
        self.assertTrue(is_passphrase_valid_anagrams("iiii oiii ooii oooi oooo"))
        self.assertFalse(is_passphrase_valid_anagrams("oiii ioii iioi iiio"))

################################################################################

if __name__ == '__main__':
    main()

################################################################################
