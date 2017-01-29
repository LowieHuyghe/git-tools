
from scriptcore.console.cuiscript import CuiScript


class Commit(CuiScript):

    def __init__(self, base_path, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param arguments:   The arguments
        """

        title = 'Git commit'
        description = 'Record changes to the repository'

        super(Commit, self).__init__(base_path, title, description, arguments=arguments)

        self._register_option('m', 'Commit message')

    def _run(self):
        """
        Actually run the script
        """

        if self._has_option('m'):
            message = self._get_option('m')
        else:
            message = self.input('Specify your commit message:')

        if not message:
            self.output('No message specified', 'error')
        else:
            message.replace('"', "'")
            self.execute('git commit -m "%s"' % message)
            self.execute('git rev-parse HEAD | pbcopy')
