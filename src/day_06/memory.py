__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List


################################################################################

class Memory:

    def __init__(self, banks: List[int]):
        """
        A memory consists of a number of memory banks. Each bank can hold any
        number of blocks.

        :param banks: list of integers, one for each memory bank; each number is
        number of already allocated blocks
        """

        self._banks = banks
        self._cycles = 0
        self._loop_size = 0
        self._states = []

################################################################################

    @property
    def cycles(self) -> int:
        """
        :return: how many redistributions can be done before a blocks-in-banks
        configuration is produced that has been seen before
        """

        return self._cycles

################################################################################

    @property
    def loop_size(self) -> int:
        """
        :return: starting from a state that has already been seen (found by
        running the redistribution loop once), how many block redistribution
        cycles must be performed before that same state is seen again
        """

        return self._loop_size

################################################################################

    def run_debugger(self) -> None:
        """
        The debugger would like to know how many redistributions can be done
        before a blocks-in-banks configuration is produced that has been seen
        before. Run the redistribution loop until this state is found.

        The debugger would also like to know the size of the loop: starting from
        a state that has already been seen (found by running the redistribution
        loop once), how many block redistribution cycles must be performed
        before that same state is seen again?
        """

        # run the redistribution loop until the banks are in a state that has
        # already been seen before
        while tuple(self._banks) not in self._states:
            self._states.append(tuple(self._banks))
            self._redistribute()
            self._cycles += 1

        # mark the state that has already been seen before
        state = tuple(self._banks)
        # run the redistribution loop again until the banks are in the marked
        # state again
        while True:
            self._redistribute()
            self._loop_size += 1

            if tuple(self._banks) == state:
                break

################################################################################

    def _redistribute(self) -> None:
        """
        Find the memory bank with the most blocks (ties won by the
        lowest-numbered memory bank) and redistribute those blocks among the
        banks. To do this, remove all the blocks from the selected bank, move to
        the next (by index) memory bank and insert one of the blocks. Continue
        doing this until we run out of blocks; if we reach the last memory bank,
        wrap around to the first one.
        """

        # find the memory with the most blocks
        blocks = max(self._banks)
        bank_index = self._banks.index(blocks)
        # remove all the blocks from the selected bank
        self._banks[bank_index] = 0

        # continue doing this until we run out of blocks
        while blocks > 0:
            # move to the next bank
            bank_index += 1
            # if we reach last memory bank, wrap around to the first one
            bank_index %= len(self._banks)
            # insert one of the blocks
            self._banks[bank_index] += 1
            blocks -= 1

################################################################################
