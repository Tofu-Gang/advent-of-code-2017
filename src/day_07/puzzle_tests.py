__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_07.tower import Tower


################################################################################

class TestDay01(TestCase):
    LINES = ("pbga (66)\n"
             "xhth (57)\n"
             "ebii (61)\n"
             "havc (66)\n"
             "ktlj (57)\n"
             "fwft (72) -> ktlj, cntj, xhth\n"
             "qoyq (66)\n"
             "padx (45) -> pbga, havc, qoyq\n"
             "tknk (41) -> ugml, padx, fwft\n"
             "jptl (61)\n"
             "ugml (68) -> gyxo, ebii, jptl\n"
             "gyxo (61)\n"
             "cntj (57)").split("\n")

################################################################################

    def test_puzzle_1(self) -> None:
        """
        For example, if your list is the following:
        pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)

        ...then you would be able to recreate the structure of the towers that
        looks like this:
                        gyxo
                      /
                 ugml - ebii
               /     \\
              |         jptl
              |
              |         pbga
             /        /
        tknk --- padx - havc
            \\       \\
              |         qoyq
              |
              |         ktlj
              \\      /
                 fwft - cntj
                      \
                        xhth

        In this example, tknk is the bottom program.
        """

        tower = Tower(self.LINES)
        self.assertEqual(tower.get_bottom_program().name, "tknk")

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For tknk to be balanced, each of the programs standing on its disc and
        all programs above it must each match. This means that the following
        sums must all be the same:
        ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
        padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
        fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

        As you can see, tknk's disc is unbalanced: ugml's stack is heavier than
        the other two. Even though the nodes above ugml are balanced, ugml
        itself is too heavy: it needs to be 8 units lighter for its stack to
        weigh 243 and keep the towers balanced. If this change were made, its
        weight would be 60.
        """

        tower = Tower(self.LINES)
        self.assertEqual(tower.get_balanced_weight(), 60)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
