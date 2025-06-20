__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple


################################################################################

class KnotHash:
    SPARSE_HASH_ROUNDS_COUNT = 64
    LENGTHS_SUFFIX = (17, 31, 73, 47, 23)
    XOR_BLOCK_LENGTH = 16

################################################################################

    def __init__(self, lengths: str, marks: Tuple[int, ...]):
        """
        This hash function simulates tying a knot in a circle of string with
        marks on it (second param). Based on the input to be hashed, the
        function repeatedly selects a span of string (length based on first
        param), brings the ends together, and gives the span a half-twist to
        reverse the order of the marks within it. After doing this for each
        length, the order of the marks is used to build the resulting hash.

        :param lengths: input list of lengths
        :param marks: input list of marks
        """

        try:
            self._lengths = tuple(map(int, lengths.split(",")))
        except ValueError:
            # empty list of lengths
            self._lengths = tuple()
        # treat each character as a byte - to create a byte, get character ASCII
        # value
        self._lengths_ascii = \
            tuple(map(ord, tuple(lengths))) + self.LENGTHS_SUFFIX
        self._marks = list(marks)
        # current position in the marks list
        self._position = 0
        # after each step, jump forward by the length of the reversed marks
        # sub-set plus this value
        self._skip_size = 0

################################################################################

    @property
    def multiplication(self) -> int:
        """
        :return: the result of multiplying the first two numbers in the marks
        list, after doing one round of knot hash algorithm (for puzzle 1)
        """

        self._do_one_round(self._lengths)
        return self._marks[0] * self._marks[1]

################################################################################

    @property
    def knot_hash(self) -> str:
        """
        :return: knot hash for puzzle 2
        """

        for _ in range(self.SPARSE_HASH_ROUNDS_COUNT):
            # repeat one round of the knot hash algorithm multiple times
            self._do_one_round(self._lengths_ascii)

        result = ""

        while len(self._marks) > 0:
            # take a specified count of numbers from the marks list
            subset = self._marks[:self.XOR_BLOCK_LENGTH]
            self._marks = self._marks[self.XOR_BLOCK_LENGTH:]
            # XOR together the numbers
            sub_result = subset[0]
            for number in subset[1:]:
                sub_result ^= number
            # convert the result to HEX and pad it with leading zero if
            # necessary
            result += "{:02x}".format(sub_result)

        return result

################################################################################

    def _do_one_round(self, lengths: Tuple[int, ...]) -> None:
        """
        Perform one round of the knot hash algorithm.
        """

        for length in lengths:
            # get "length" long subset of marks, starting on the current
            # position (treat the marks list as circular)
            pre_wrap_from = self._position
            pre_wrap_to = min(self._position + length, len(self._marks))
            post_wrap_from = 0
            post_wrap_to = max(self._position + length - len(self._marks), 0)
            pre_wrap_len = pre_wrap_to - pre_wrap_from
            sublist = (self._marks[pre_wrap_from:pre_wrap_to] +
                       self._marks[post_wrap_from:post_wrap_to])
            # reverse it
            sublist.reverse()
            # replace the original subset with the reversed one
            self._marks[pre_wrap_from:pre_wrap_to] = sublist[:pre_wrap_len]
            self._marks[post_wrap_from:post_wrap_to] = sublist[pre_wrap_len:]
            # jump forward past the reversed subset
            self._position += length
            # jump further by the specified number of steps
            self._position += self._skip_size
            # wrap around if necessary
            self._position %= len(self._marks)
            # increase the final jump for the next step
            self._skip_size += 1

################################################################################
