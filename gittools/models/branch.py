
from scriptcore.basescript import BaseScript
import re


class Branch(object):

    @staticmethod
    def all():
        """
        Get all branches
        :return:    List of Branch's
        """

        current_script = BaseScript.current_script()
        out, err, exitcode = current_script.execute('git branch')

        branches = []
        for line in out:
            match = re.match('^(\*?)\s*(.+)$', line)

            name = match.group(2)
            current = match.group(1) == '*'

            if not name:
                continue

            branches.append(Branch(name, current))

        return branches

    def __init__(self, name, current):
        """
        Constructor
        :param name:    Name of the branch
        :param current: Current branch
        """

        self.name = name
        self.current = current
