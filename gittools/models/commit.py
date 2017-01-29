
from scriptcore.basescript import BaseScript


class Commit(object):

    @staticmethod
    def all(limit=10):
        """
        Get all commits
        :param limit:   The limit
        :return:        List of Commit's
        """

        current_script = BaseScript.current_script()
        output = current_script.execute('git log -n %i --pretty=format:"%%H | \%%h | %%ai | %%an <%%ae> | %%s"' % limit)

        commits = []
        for line in output:
            parts = line.split(' | ')

            commits.append(Commit(parts[0], parts[1], parts[3], parts[4], parts[2]))

        return commits

    @staticmethod
    def where(where, limit=10):
        """
        Get filtered commits
        :param where:   Where statement
        :param limit:   The limit
        :return:        List of Commit's
        """

        current_script = BaseScript.current_script()
        output = current_script.execute('git log -n %i %s --pretty=format:"%%H | \%%h | %%ai | %%an <%%ae> | %%s"' % (limit, where))

        commits = []
        for line in output:
            parts = line.split(' | ')

            commits.append(Commit(parts[0], parts[1], parts[3], parts[4], parts[2]))

        return commits

    def __init__(self, full_hash, short_hash, author, message, datetime):
        """
        Constructor
        :param full_hash:   The full hash
        :param short_hash:  The short hash
        :param author:      The author
        :param message:     The message
        :param datetime:    The date time
        """
        self.full_hash = full_hash
        self.short_hash = short_hash
        self.author = author
        self.message = message
        self.datetime = datetime
