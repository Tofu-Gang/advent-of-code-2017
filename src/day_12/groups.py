__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List, Dict, Tuple, Set, Any


################################################################################

class Groups:
    SEP_1 = "<->"
    SEP_2 = ","

################################################################################

    def __init__(self, programs_list: List[str]):
        """
        Parse program connections from the initial input list. Sort the programs
        into groups.

        :param programs_list: the initial connections list
        """

        self._connections = self._parse_connections(programs_list)
        self._groups = self._parse_groups()

################################################################################

    @property
    def groups_count(self) -> int:
        """
        :return: number of groups
        """

        return len(self._groups)

################################################################################

    def get_group_size(self, program_id: str) -> int:
        """
        :param program_id: a program id
        :return: size of the group which the specified program is a member of
        """

        return len(self._get_group(program_id))

################################################################################

    def _get_group(self, program_id: str) -> Set[str]:
        """
        :param program_id: a program id
        :return: the group which the specified program is a member of
        """

        return next(filter(lambda group: program_id in group, self._groups))

################################################################################

    def _parse_connections(self, programs_list: List[str]) \
            -> Dict[str, Tuple[str, ...]]:
        """
        :param programs_list: list of lines from the puzzle input
        :return: dict of connections, where key is a program id and value is a
        tuple of program ids with which the key program can communicate directly
        """

        return dict(
            (line.split(self.SEP_1)[0].strip(),
             tuple(map(str.strip,line
                       .split(self.SEP_1)[1]
                       .strip().split(self.SEP_2))))
            for line in programs_list)

################################################################################

    def _parse_groups(self) -> Tuple[Any, ...]:
        """
        :return: tuple of groups, where each group is a set of program ids that
        can communicate together either directly or via other programs in the
        group
        """

        groups = []

        while len(self._connections) > 0:
            # get a connection record, make it a group and remove the connection
            # record
            key = tuple(self._connections.keys())[0]
            group = set()
            group.update(key)
            group.update(self._connections[key])
            del self._connections[key]

            # go through the group and for each program in the group, look for
            # a connection record associated with it
            while any(program_id in self._connections for program_id in group):
                for program_id in group:
                    if program_id in self._connections:
                        # if it exists, upgrade the group with this connection
                        # record and then remove it
                        group.update(self._connections[program_id])
                        del self._connections[program_id]
                        break

            groups.append(group)

        return tuple(groups)

################################################################################
