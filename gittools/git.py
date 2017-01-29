
from scriptcore.console.cuiscript import CuiScript
from gittools.commands.checkout import Checkout
from gittools.commands.commit import Commit
from gittools.commands.show import Show
from gittools.commands.pick import Pick


class Git(CuiScript):

    def __init__(self, base_path, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param arguments:   The arguments
        """

        title = 'Git'
        description = 'Helpers for git'

        super(Git, self).__init__(base_path, title, description, arguments=arguments)

        self._register_command('checkout', 'Switch branches', Checkout)
        self._register_command('commit', 'Record changes to the repository', Commit)
        self._register_command('show', 'Show various types of objects', Show)
        self._register_command('pick', 'Pick various types of objects', Pick)
