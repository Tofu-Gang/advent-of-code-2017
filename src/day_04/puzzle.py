__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a 
passphrase instead of simply a password. A passphrase consists of a series of 
words (lowercase letters) separated by spaces.
"""

from src.utils.utils import print_puzzle_solution


################################################################################

INPUT_FILE_PATH = "src/day_04/input.txt"

################################################################################

def is_passphrase_valid(passphrase: str) -> bool:
    """
    For puzzle 1.
    A passphrase is valid if it does not contain anz duplicate words.

    :param passphrase: a passphrase to test
    :return: True if the passphrase is valid, False otherwise
    """

    words = passphrase.strip().split()
    return len(set(words)) == len(words)

################################################################################

def is_passphrase_valid_anagrams(passphrase: str) -> bool:
    """
    For puzzle 2.
    A passphrase is valid if it does not contain any two words that are anagrams
    of each other.

    :param passphrase: a passphrase to test
    :return: True if the passphrase is valid, False otherwise
    """

    words = tuple(map(
        lambda word: "".join(sorted(word)),
        passphrase.strip().split()))
    return len(set(words)) == len(words)

################################################################################

def puzzle_01() -> None:
    """
    To ensure security, a valid passphrase must contain no duplicate words.

    For example:
    -aa bb cc dd ee is valid.
    -aa bb cc dd aa is not valid - the word aa appears more than once.
    -aa bb cc dd aaa is valid - aa and aaa count as different words.

    The system's full passphrase list is available as your puzzle input. How
    many passphrases are valid?

    :return: None; Answer should be 383.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        passphrases = f.read().split("\n")
        result = len(
            tuple(filter(bool, [
                is_passphrase_valid(passphrase)
                for passphrase in passphrases])))
        print_puzzle_solution(result)

################################################################################

def puzzle_02() -> None:
    """
    For added security, yet another system policy has been put in place. Now, a
    valid passphrase must contain no two words that are anagrams of each other -
    - that is, a passphrase is invalid if any word's letters can be rearranged
    to form any other word in the passphrase.

    For example:
    -abcde fghij is a valid passphrase.
    -abcde xyz ecdab is not valid - the letters from the third word can be
     rearranged to form the first word.
    -a ab abc abd abf abj is a valid passphrase, because all letters need to be
     used when forming another word.
    -iiii oiii ooii oooi oooo is valid.
    -oiii ioii iioi iiio is not valid - any of these words can be rearranged to
     form any other word.

    Under this new system policy, how many passphrases are valid?

    :return: None; Answer should be 265.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        passphrases = f.read().split("\n")
        result = len(
            tuple(filter(bool, [
                is_passphrase_valid_anagrams(passphrase)
                for passphrase in passphrases])))
        print_puzzle_solution(result)

################################################################################