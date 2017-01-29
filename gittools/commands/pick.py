
from scriptcore.console.cuiscript import CuiScript
from gittools.models.commit import Commit


class Pick(CuiScript):

    def __init__(self, base_path, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param arguments:   The arguments
        """

        title = 'Git pick'
        description = 'Pick various types of objects'

        super(Pick, self).__init__(base_path, title, description, arguments=arguments)

        self._register_option('l', 'Pick latest')
        self._register_option('a', 'Pick from given author')

    def _run(self):
        """
        Actually run the script
        """

        # Fetch commits
        if self._has_option('a'):
            commits = Commit.where('--author=' + self._get_option('a'))
        else:
            commits = Commit.all()

        # Pick commit
        if self._has_option('l'):
            commit = commits[0]
        else:
            commit_descriptions = []
            for commit in commits:
                commit_description = '%s %s %s\n        %s' % (
                    self.output.color(commit.short_hash, 'gray_dark'),
                    self.output.color(commit.author, 'green'),
                    self.output.color('on %s' % commit.datetime, 'gray_dark'),
                    commit.message
                )
                commit_descriptions.append(commit_description)

            index = self.input.pick(commit_descriptions, 'Pick your commit:')
            if index is not None:
                commit = commits[index]
            else:
                commit = None

        # Pick commit
        if commit:
            self.execute('echo "*%s* _%s_" | pbcopy' % (commit.full_hash, commit.message))
            self.output('Copied to clipboard', 'success')
        else:
            self.output('No commit to show', 'error')
