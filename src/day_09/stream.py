__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


################################################################################

class Stream:
    GROUP_OPEN = "{"
    GROUP_CLOSE = "}"
    GARBAGE_OPEN = "<"
    GARBAGE_CLOSE = ">"
    CANCELLED = "!"

################################################################################

    def __init__(self, characters: str):
        """
        Save the characters in the stream. The goal is to count total score for
        all groups and total number of non-canceled garbage characters in the
        stream.
        """

        self._characters = characters
        self._total_score = 0
        self._garbage_count = 0

################################################################################

    @property
    def total_score(self) -> int:
        """
        :return: total score for all groups in the stream
        """

        return self._total_score

################################################################################

    @property
    def garbage_count(self) -> int:
        """
        :return: number of all non-canceled garbage characters in the stream
        """

        return self._garbage_count

################################################################################

    def process_stream(self) -> None:
        """
        Go through all characters in the stream, parse out groups and count
        their total score. Also, count all non-canceled garbage characters.
        """

        # flag is True while between <>
        garbage = False
        # flag is True for exactly one character after !
        cancelled = False
        # current innermost group score; the outermost group that includes the
        # entire input stream has score of one
        score = 0

        for character in self._characters:
            if cancelled:
                # the character is canceled
                cancelled = False
                continue
            elif character == self.CANCELLED:
                # next character is canceled
                cancelled = True
                continue
            elif garbage:
                # inside garbage
                if character == self.GARBAGE_CLOSE:
                    # end of garbage
                    garbage = False
                else:
                    # count in non-canceled garbage character
                    self._garbage_count += 1
                    continue
            elif character == self.GARBAGE_OPEN:
                # entering garbage
                garbage = True
                continue
            elif character == self.GROUP_OPEN:
                # entering group
                score += 1
                continue
            elif character == self.GROUP_CLOSE:
                # leaving group
                self._total_score += score
                score -= 1
                continue

################################################################################
