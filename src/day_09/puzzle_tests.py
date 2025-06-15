__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_09.stream import Stream


################################################################################

class TestDay01(TestCase):

    def test_puzzle_1(self) -> None:
        """
        Your goal is to find the total score for all groups in your input. Each
        group is assigned a score which is one more than the score of the group
        that immediately contains it. (The outermost group gets a score of 1.)
        -{}, score of 1.
        -{{{}}}, score of 1 + 2 + 3 = 6.
        -{{},{}}, score of 1 + 2 + 2 = 5.
        -{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
        -{<a>,<a>,<a>,<a>}, score of 1.
        -{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
        -{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
        -{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
        """

        stream = Stream("{}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 1)
        stream = Stream("{{{}}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 6)
        stream = Stream("{{},{}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 5)
        stream = Stream("{{{},{},{{}}}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 16)
        stream = Stream("{<a>,<a>,<a>,<a>}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 1)
        stream = Stream("{{<ab>},{<ab>},{<ab>},{<ab>}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 9)
        stream = Stream("{{<!!>},{<!!>},{<!!>},{<!!>}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 9)
        stream = Stream("{{<a!>},{<a!>},{<a!>},{<ab>}}")
        stream.process_stream()
        self.assertEqual(stream.total_score, 3)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        Count all of the characters within the garbage. The leading and trailing
        < and > don't count, nor do any canceled characters or the ! doing the
        canceling.
        -<>, 0 characters.
        -<random characters>, 17 characters.
        -<<<<>, 3 characters.
        -<{!>}>, 2 characters.
        -<!!>, 0 characters.
        -<!!!>>, 0 characters.
        -<{o"i!a,<{i<a>, 10 characters.
        """

        stream = Stream("<>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 0)
        stream = Stream("<random characters>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 17)
        stream = Stream("<<<<>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 3)
        stream = Stream("<{!>}>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 2)
        stream = Stream("<!!>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 0)
        stream = Stream("<!!!>>")
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 0)
        stream = Stream('<{o"i!a,<{i<a>')
        stream.process_stream()
        self.assertEqual(stream.garbage_count, 10)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
